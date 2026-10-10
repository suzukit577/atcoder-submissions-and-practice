# Repository Guidelines

## Purpose

AtCoderのコンテスト参加、問題演習、競技プログラミング用ライブラリ、ヒューリスティックの実験をまとめる個人用リポジトリ。

## README Authority

`README.md`は、ユーザーが最終化した公開方針の正本とする。リポジトリの目的、ディレクトリ概要、記録と保守の範囲、使用環境、コードの所有と出典、生成AIの利用方針、ライセンスと免責はREADMEを優先する。

- ユーザーがREADMEの再編集を明示的に依頼しない限り、READMEを変更しない。
- READMEと`AGENTS.md`、`REVIEW.md`、その他の文書が競合する場合は、READMEを維持し、従属する規則や文書を修正する。
- READMEのディレクトリ構成はtext treeを正本とする。構成変更時はtreeを実際のtop-level directoryと整合させ、表への置換を提案しない。
- 過去の提出・練習codeへ、READMEが目的としていないportfolio品質、模範解答としての正しさ、現在のstyleへの統一を要求しない。
- `heuristic/`に現時点でcodeがないことや、過去codeに改善余地があることをrepository不備として扱わない。

## AI Assistance Boundary

このリポジトリでの競技プログラミングは、ユーザー本人の問題解決力、コーディング力、アルゴリズムとデータ構造への理解を高めることが目的。AIは、その能力形成を代替または補助する役割を持たない。この境界は、過去問の練習にも適用する。

AIは次の作業を行わない。

- 問題文の要約、問題理解の補助、着眼点の提示
- 解法、アルゴリズム、データ構造、証明、計算量の提案や説明
- 提出コードや練習コードの作成、補完、書き換え、最適化
- 提出コードや練習コードのデバッグ、テスト、実行結果の分析
- ユーザー本人が考えた解法の正誤判定や改善案の提示
- コンテスト成績やスコアへ直接影響する支援

AIの作業範囲は次に限定する。

- ディレクトリやファイルの移動、命名、分割、分類
- README、AGENTS.md、設定ファイルなどの整備
- 過去コードのロジックを変えない機械的な整理
- スニペット管理を目的とした`mylib/`の構成整理、保守、テスト
- `mylib/`を原本とするVS Codeスニペットの生成と同期
- 生成物、仮想環境、Git管理対象の整理

依頼が許可範囲か曖昧な場合は、競技力への支援を行わず、ユーザーへ境界を確認する。`algorithm/`、`training/`、`heuristic/`のコードへ機械的でない変更を加えない。

### Contest Rules

開催中のコンテストでは、ユーザーの個人方針に加えて最新の公式規則を必ず優先する。生成AIの使用が禁止されるコンテストでは、生成AIを一切使用しない。問題文、コード、エラー、実行結果、スコアをAIへ入力しない。

2026年10月4日時点の確認結果は次の通り。

- 開催中のABC・ARC・AGCでは生成AIの使用を原則禁止
- 開催中の短期AHCでも生成AIの使用を原則禁止
- 長期AHCには別ルールが適用され、一定の利用が許可される一方、大量の候補を自動生成・評価・選別する利用は禁止
- 過去問練習は公式の開催中ルールの対象外だが、このリポジトリでは上記の個人方針を適用

長期AHCなど規則上AIを利用できる場合でも、利用を自動的に許可しない。参加時点の公式規則を再確認し、ユーザーがそのコンテストでのAI利用を明示的に決めた場合だけ、許可範囲を個別に定める。

- [ABC・ARC・AGCの生成AI対策ルール](https://info.atcoder.jp/entry/llm-rules-ja)
- [短期AHCの生成AI利用ルール](https://info.atcoder.jp/entry/short-ahc-llm-rules-ja)
- [長期AHCに適用される生成AI利用ルール](https://info.atcoder.jp/entry/ahc-llm-rules-ja)

## Local-only Context

- 開催中は対象コンテストの最新の公式規則を先に確認し、許可用途に該当すると確認できないAI、外部Context、Agent toolを使用しない。
- Local-onlyなAgent設定と外部から取得した非公開Contextは、このrepositoryの正本ではなく、tracked fileへ複写しない。Code、test、READMEを実装上の正本とする。
- Commit前にstaged diffを確認し、credential、個人の絶対path・識別子、未承認のprivate materialを除外する。

## Cross-Agent Review

Cross-Agent基盤は、このリポジトリのAI利用境界を緩和しない。Codexを主実装Agent、Claude Codeを独立reviewerとして利用できるのは、上記の許可範囲に限る。最終判断はユーザーが行う。

共通の実装規律は、[Karpathy Guidelinesの固定revision](https://github.com/multica-ai/andrej-karpathy-skills/blob/64723a49ea6117894304eb491f0d32a60570bf45/skills/karpathy-guidelines/SKILL.md)を直接参照する。原則本文はこのリポジトリへ複製しない。このリポジトリではAI Assistance BoundaryとContest Rulesが常に優先し、外部ガイドラインを理由に解法codeの生成、評価、改善へscopeを広げない。

- Reviewの一次資料は、requirement、repository、Git diff、test結果とする。
- Claude Codeは`REVIEW.md`に従い、明示的に修正を依頼されない限りfileを変更しない。
- Claude Codeのfindingはそのまま採用しない。Codexがrepository evidenceとrequirementを確認し、`VALID`、`PARTIALLY_VALID`、`INVALID`に分類してから、成立する問題だけを修正する。
- `algorithm/`、`training/`、`heuristic/`の解法codeは、Cross-Agentによるsemantic reviewの対象外とする。File移動等の機械的変更は、内容をAIへ評価させず、layout test、Git diff、生成物検査で確認する。
- `mylib/`のreviewは、開催中コンテストと無関係であり、ユーザーが明示的に依頼した保守、test、snippet同期に限る。Contest問題を入力として新しい解法やalgorithmを作らせない。
- 開催中コンテストの問題文、code、error、実行結果、scoreを含むdiffは、Claude Codeへ渡さない。該当する可能性がある場合はreviewを開始せず、ユーザーへ確認する。
- Review対象と無関係な過去の提出codeをClaude Codeのcontextへ追加しない。
- Repositoryの公開、public release、第三者由来fileの追加時は、`REVIEW.md`のPublication Readiness Reviewを適用する。解法のsemantic reviewは行わず、authorship、source、license、利用規約、再配布条件、Git historyだけを確認する。

### Shared and Local Agent Files

- `AGENTS.md`、`CLAUDE.md`、`REVIEW.md`は、repository共通の契約としてGit管理する。
- `.claude/settings.json`を追加する場合は、共有すべきpermission、hook、pluginだけを置く。Credential、個人path、private endpoint、任意commandを許可するbroad permissionを含めない。
- `CLAUDE.local.md`、`.claude/settings.local.json`、`.agent-handoff.md`はlocal-onlyとし、Git管理しない。
- Agent instructionとshared permissionを変更するときは、Agentが読めるfile、実行できるcommand、外部送信先が増えないか確認する。
- Securityをinstructionの非公開性へ依存させず、必要な制約はtest、hook、CI、permissionでも強制する。

## General Policy

- 新しいディレクトリ名は小文字で統一する。
- `algorithm/`と`training/`の既存コードは、当時の提出・練習記録として扱う。
- 継続的な保守対象は主に`mylib/`、`scripts/`、`snippets/`、`tests/`とし、再利用codeの変更時は関連testとVS Code snippetの同期を確認する。
- `algorithm/`、`training/`、`heuristic/`へ置く解法codeは、ユーザー本人が作成したものに限定する。
- 公式解説や第三者解説はsource URLだけを記録し、本文、画像、sample code、写経、言語翻訳をGit管理しない。
- 過去コードの一括整形、リファクタリング、解法変更は、明示的な依頼がない限り行わない。
- 1つのPythonファイルには、原則として1つの実行可能な解法だけを置く。
- `.DS_Store`、`*.out`、仮想環境、入力・出力・ログなどの生成物をGit管理へ追加しない。
- Python仮想環境はルートの`.venv/`を使用し、別名の仮想環境をリポジトリ内に作らない。
- コミットは明示的に依頼された場合だけ作成する。

## Directory Roles

- `algorithm/`: アルゴリズム系コンテストの提出コードと別解
- `training/`: 問題集・学習コース単位の練習コード
- `mylib/`: 継続的に保守・テストする再利用コード
- `heuristic/`: AtCoder Heuristic Contestの提出コードと実験記録
- `scripts/`: リポジトリ整備と生成処理
- `snippets/`: `mylib/`から生成したVS Codeスニペット
- `tests/`: `mylib/`と整備スクリプトのテスト

`training/topics/`のようなテーマ別分類は常設しない。必要になった場合だけ、既存コードを調査してから追加する。

## Solution Files

提出コードまたは最初の自作解法は`<problem>.py`へ保存し、追加の自作解法には次の接尾辞を使う。

- `_alternative`: 別解
- `_reimplementation`: 解説を理解した後、code表現をコピーせず独立して書いた実装

同種の解法が複数ある場合は`_1`、`_2`を追加する。詳細は`algorithm/README.md`を参照。

`_official`、`_evima`、`_user`、`_commentary`、`_original_author`は第三者由来codeと誤認しやすいため使用しない。参考資料がある場合は、codeを転載せずsource URLをコメントまたはREADMEへ記録する。

明示的な見出しで連結された解法の確認には次を使う。

```bash
uv run python scripts/split_solution_sections.py --check
```

見出しのないコードを機械的に分割しない。入力処理の回数だけでは、複数解法か1つの解法かを安全に判定できない。

## Library

`mylib/`だけを継続的なリファクタリング対象とする。

- ディレクトリ名、モジュール名、関数名はスネークケースを基本とする。
- 各モジュールは、可能な限り単体で提出コードへコピーできる形にする。
- 入力条件、返り値、計算量をdocstringへ記載する。
- 新規実装や仕様変更には`tests/library_tests/`のテストを追加する。
- 空のプレースホルダファイルは作らない。
- 実装されていないアルゴリズムは、必要になった時点でコードとテストを同時に追加する。

## VS Code Snippets

スニペット本体の原本は`mylib/`のPythonファイル。生成済みJSONを直接編集しない。

- スニペット名、prefix、対象ファイルは`mylib/snippets.toml`で管理する。
- `mylib/`を変更したらスニペットを再生成する。
- 生成後は`--check`で同期を確認する。

```bash
uv run python scripts/generate_vscode_snippets.py
uv run python scripts/generate_vscode_snippets.py --check
```

生成先は`snippets/atcoder.code-snippets`。ローカルのVS Codeグローバルスニペットは、この生成ファイルへのシンボリックリンクを使用する。

## Heuristic Contests

コンテストごとに`heuristic/ahc/ahcxxx/`を作り、基本構成を次の形にする。

```text
ahcxxx/
  main.py
  README.md
  tools/
  in/
  out/
  logs/
```

- `main.py`: 提出コード
- `README.md`: 方針、スコア、試した改善、最終提出の記録
- `tools/`: ローカルテスタや補助スクリプト
- `in/`、`out/`、`logs/`、`target/`: Git管理外の生成物

## Documentation Style

- このリポジトリは個人開発・競技記録用のプロジェクトである。リポジトリ自身や成果物を`product`、プロダクト、製品と呼ばず、プロジェクト、記録、実装、ライブラリを使う。外部仕様の正式名称等、別概念のcanonical termは維持する。
- READMEやリポジトリ内の説明文は日本語を基本とする。
- READMEは、公開時に初めて読む利用者へ向けた文書として`です・ます`調で記載する。
- README以外の開発文書は、常体または体言止めで統一する。
- `〜している`、`〜していく`を繰り返さず、簡潔な説明にする。

## Verification

変更後は、対象に応じて次を実行する。

```bash
uv run python -m unittest discover -s tests
uv run mypy mylib scripts tests
uv run ruff check mylib scripts tests
uv run ruff format --check mylib scripts tests
uv run ruff check --select F821,F822,F823 algorithm training
uv run python scripts/generate_vscode_snippets.py --check
uv run python scripts/split_solution_sections.py --check
git diff --check
git diff --cached --check
```

`algorithm/`と`training/`全体へフォーマッタを適用しない。これらには過去の提出コードをそのまま残す。
