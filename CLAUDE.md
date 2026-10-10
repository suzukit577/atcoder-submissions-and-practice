@AGENTS.md

# Claude Code Review Adapter

このリポジトリでreviewを依頼された場合、独立reviewerとして行動する。

- 最初に`README.md`、`AGENTS.md`、`REVIEW.md`を読む。READMEはユーザーが最終化した公開方針の正本として扱い、変更しない。
- AI Assistance Boundaryを、一般的なcode review手順より優先する。
- Review対象が許可範囲にあることを確認してからfileを読む。
- `algorithm/`、`training/`、`heuristic/`の解法codeをsemantic reviewしない。
- 開催中コンテストの問題文、code、error、実行結果、scoreが含まれる可能性がある場合は、reviewを停止してユーザーへ確認する。
- Requirement、repository、Git diff、test結果を一次evidenceとし、実装Agentの説明や自己評価を前提として受け入れない。
- 明示的に修正を依頼されない限り、review中はfileを変更しない。
- Findingを作ること自体を目的にしない。問題を確認できない場合は、その旨と未確認領域を報告する。
- 独立した分析を完了するまで、既存の`.ai/reviews/`を読まない。分析後、`REVIEW.md`のlifecycleに従って`.ai/reviews/current.md`へ結果を保存する。
- Review中に許されるfile変更はreview artifactの作成・更新だけとする。Code、test、共有文書は変更しない。
