"""明示的な見出しで連結された複数解法を別ファイルへ分割する。"""

import argparse
import ast
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEARCH_ROOTS = (ROOT / "algorithm", ROOT / "training")
THIRD_PARTY_SECTION_PATTERN = re.compile(
    r"^# (公式解説|evima 解説|ユーザ解説|解説\(evima\)|解説|原案者の実装)"
)
SECTION_PATTERN = re.compile(r"^# (別解|Run Length Encoding|実装例|楽な実装)")
SLUGS = {
    "別解": "alternative",
    "Run Length Encoding": "alternative",
    "実装例": "alternative",
    "楽な実装": "alternative",
}


def normalize(lines: list[str]) -> str:
    """前後の空行を除き、末尾改行を1つ付ける。"""
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "".join(lines).rstrip("\r\n") + "\n"


def split_source(path: Path) -> list[tuple[Path, str]]:
    """分割後の保存先とソースコードを返す。分割不要なら空リスト。"""
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    if any(THIRD_PARTY_SECTION_PATTERN.match(line) for line in lines):
        raise ValueError(f"third-party section header is not allowed: {path}")

    marker_indexes = [
        index for index, line in enumerate(lines) if SECTION_PATTERN.match(line)
    ]
    if not marker_indexes:
        return []

    first_marker = marker_indexes[0]
    has_source_before_marker = any(line.strip() for line in lines[:first_marker])
    boundaries = marker_indexes
    if has_source_before_marker:
        boundaries = [0, *marker_indexes]
    if len(boundaries) <= 1:
        return []

    boundaries = [*boundaries, len(lines)]
    sections = [
        normalize(lines[start:end]) for start, end in zip(boundaries, boundaries[1:])
    ]
    for section in sections:
        ast.parse(section, filename=str(path))

    tagged_sections: list[tuple[str, str]] = []
    for section in sections[1:]:
        header = section.splitlines()[0]
        match = SECTION_PATTERN.match(header)
        if match is None:
            raise ValueError(f"section header not found: {path}: {header}")
        tagged_sections.append((SLUGS[match.group(1)], section))

    slug_counts = Counter(slug for slug, _ in tagged_sections)
    slug_indexes: Counter[str] = Counter()
    result = [(path, sections[0])]
    for slug, section in tagged_sections:
        slug_indexes[slug] += 1
        suffix = slug
        if slug_counts[slug] > 1:
            suffix += f"_{slug_indexes[slug]}"
        destination = path.with_name(f"{path.stem}_{suffix}{path.suffix}")
        result.append((destination, section))
    return result


def collect_changes() -> list[tuple[Path, list[tuple[Path, str]]]]:
    """分割対象と分割結果を収集し、保存先の衝突を検証する。"""
    changes: list[tuple[Path, list[tuple[Path, str]]]] = []
    destinations: set[Path] = set()
    for search_root in SEARCH_ROOTS:
        for path in sorted(search_root.rglob("*.py")):
            split_result = split_source(path)
            if not split_result:
                continue
            for destination, _ in split_result[1:]:
                if destination in destinations or destination.exists():
                    raise FileExistsError(f"destination already exists: {destination}")
                destinations.add(destination)
            changes.append((path, split_result))
    return changes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="分割をファイルへ反映")
    parser.add_argument(
        "--check",
        action="store_true",
        help="分割対象が残っていれば終了コード1を返す",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    changes = collect_changes()
    created_count = sum(len(result) - 1 for _, result in changes)
    print(f"source files: {len(changes)}")
    print(f"new files: {created_count}")

    if args.check:
        return int(bool(changes))
    if not args.apply:
        for source, result in changes:
            destinations = ", ".join(
                str(path.relative_to(ROOT)) for path, _ in result[1:]
            )
            print(f"{source.relative_to(ROOT)} -> {destinations}")
        return 0

    for _, result in changes:
        for destination, contents in result:
            destination.write_text(contents, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
