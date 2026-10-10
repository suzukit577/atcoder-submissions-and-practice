import tempfile
import unittest
from pathlib import Path

from scripts.split_solution_sections import split_source


class SplitSolutionSectionsTest(unittest.TestCase):
    def test_self_authored_section_uses_alternative_suffix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            source_path = Path(temporary_directory) / "a.py"
            source_path.write_text("value = 1\n# 別解\nvalue = 2\n", encoding="utf-8")

            result = split_source(source_path)

        self.assertEqual(
            [path.name for path, _ in result],
            ["a.py", "a_alternative.py"],
        )

    def test_third_party_section_header_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            source_path = Path(temporary_directory) / "a.py"
            source_path.write_text(
                "value = 1\n# 公式解説\nvalue = 2\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "third-party section header"):
                split_source(source_path)


if __name__ == "__main__":
    unittest.main()
