"""mylibのPythonファイルからVS Codeスニペットを生成する。"""

import argparse
import ast
import json
import tomllib
from pathlib import Path
from typing import TypedDict, cast

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "mylib" / "snippets.toml"
DEFAULT_OUTPUT_PATH = ROOT / "snippets" / "atcoder.code-snippets"


class SnippetConfig(TypedDict):
    name: str
    prefix: str | list[str]
    path: str
    description: str


class Snippet(TypedDict):
    prefix: str | list[str]
    body: list[str]
    description: str


def source_without_module_docstring(path: Path) -> list[str]:
    """モジュールdocstringを除いたソースコードを行単位で返す。"""
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    lines = source.splitlines()
    if tree.body and isinstance(tree.body[0], ast.Expr):
        value = tree.body[0].value
        if isinstance(value, ast.Constant) and isinstance(value.value, str):
            del lines[tree.body[0].lineno - 1 : tree.body[0].end_lineno]
            while lines and not lines[0]:
                lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return lines


def load_snippets() -> dict[str, Snippet]:
    """設定とmylibのソースコードからスニペットを構築する。"""
    with CONFIG_PATH.open("rb") as config_file:
        raw_config = tomllib.load(config_file)

    snippets: dict[str, Snippet] = {}
    for raw_entry in raw_config["snippet"]:
        entry = cast(SnippetConfig, raw_entry)
        source_path = CONFIG_PATH.parent / entry["path"]
        snippets[entry["name"]] = {
            "prefix": entry["prefix"],
            "body": source_without_module_docstring(source_path),
            "description": entry["description"],
        }
    return snippets


def render_snippets() -> str:
    """スニペットをJSONとして描画する。"""
    return json.dumps(load_snippets(), ensure_ascii=False, indent=2) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    parser.add_argument(
        "--check",
        action="store_true",
        help="生成済みファイルが最新か確認し、差異があれば終了コード1を返す",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_path = args.output.expanduser().resolve()
    rendered = render_snippets()

    if args.check:
        if (
            not output_path.exists()
            or output_path.read_text(encoding="utf-8") != rendered
        ):
            print(f"snippet file is outdated: {output_path}")
            return 1
        print(f"snippet file is up to date: {output_path}")
        return 0

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")
    print(f"generated: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
