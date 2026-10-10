import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_LOCAL_FILES = {
    ".agent-handoff.md",
    ".claude/settings.local.json",
    "CLAUDE.local.md",
}
FORBIDDEN_LOCAL_PREFIXES = (".ai/reviews/",)
FORBIDDEN_SOLUTION_MARKERS = (
    "_commentary",
    "_evima",
    "_official",
    "_original_author",
    "_user",
)
SOLUTION_SOURCE_SUFFIXES = {".c", ".cpp", ".py"}
SOLUTION_STEM_PATTERN = re.compile(
    r"^[A-Za-z0-9-]+(?:_(?:alternative|reimplementation)(?:_[1-9][0-9]*)?)?$"
)


class RepositoryLayoutTest(unittest.TestCase):
    def tracked_files(self) -> list[Path]:
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
        paths = [Path(path) for path in result.stdout.decode().split("\0") if path]
        return [path for path in paths if (ROOT / path).is_file()]

    def test_private_and_generated_files_are_not_tracked(self) -> None:
        for path in self.tracked_files():
            normalized = path.as_posix()
            self.assertNotIn(normalized, FORBIDDEN_LOCAL_FILES)
            for prefix in FORBIDDEN_LOCAL_PREFIXES:
                self.assertFalse(normalized.startswith(prefix), normalized)
            self.assertNotEqual(path.name, ".DS_Store")
            self.assertNotEqual(path.suffix, ".out")

    def test_third_party_solution_suffixes_are_not_tracked(self) -> None:
        solution_roots = {"algorithm", "heuristic", "training"}
        for path in self.tracked_files():
            if not path.parts or path.parts[0] not in solution_roots:
                continue
            if path.suffix.lower() not in SOLUTION_SOURCE_SUFFIXES:
                continue
            for marker in FORBIDDEN_SOLUTION_MARKERS:
                self.assertNotIn(marker, path.stem, path.as_posix())

    def test_solution_file_names_follow_convention(self) -> None:
        for path in self.tracked_files():
            if not path.parts or path.parts[0] not in {"algorithm", "training"}:
                continue
            if path.suffix.lower() not in SOLUTION_SOURCE_SUFFIXES:
                continue
            self.assertRegex(path.stem, SOLUTION_STEM_PATTERN, path.as_posix())

    def test_solution_source_files_are_not_empty(self) -> None:
        for path in self.tracked_files():
            if not path.parts or path.parts[0] not in {
                "algorithm",
                "heuristic",
                "training",
            }:
                continue
            if path.suffix.lower() not in SOLUTION_SOURCE_SUFFIXES:
                continue
            self.assertGreater((ROOT / path).stat().st_size, 0, path.as_posix())

    def test_explicit_solution_sections_are_split(self) -> None:
        subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "split_solution_sections.py"),
                "--check",
            ],
            cwd=ROOT,
            check=True,
        )


if __name__ == "__main__":
    unittest.main()
