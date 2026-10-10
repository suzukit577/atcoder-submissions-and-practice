# My Library

競技プログラミングで再利用するPythonコードの原本。

各モジュールは単体でコピーできる形を基本とし、入力条件、返り値、計算量をdocstringに記載。動作確認は`tests/library_tests/`に集約。

## VS Code Snippets

VS Code用スニペットは`mylib/snippets.toml`を設定として、各Pythonファイルから自動生成。

```bash
uv run python scripts/generate_vscode_snippets.py
```

生成先は`snippets/atcoder.code-snippets`。生成ファイルは直接編集せず、修正は`mylib/`のPythonファイルへ反映。

## Test

```bash
uv run python -m unittest discover -s tests
```
