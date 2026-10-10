import ast
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNIPPET_PATH = ROOT / "snippets" / "atcoder.code-snippets"


class SnippetGenerationTest(unittest.TestCase):
    def test_generated_snippets_are_current_and_valid_python(self) -> None:
        subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "generate_vscode_snippets.py"),
                "--check",
            ],
            cwd=ROOT,
            check=True,
        )
        snippets = json.loads(SNIPPET_PATH.read_text(encoding="utf-8"))
        self.assertEqual(len(snippets), 20)
        self.assertEqual(
            snippets["3D cumulative sum"]["prefix"],
            ["build_cumulative_sum_3d", "query_cumulative_sum_3d"],
        )
        for name, snippet in snippets.items():
            with self.subTest(name=name):
                ast.parse("\n".join(snippet["body"]))


if __name__ == "__main__":
    unittest.main()
