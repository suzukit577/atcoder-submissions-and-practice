# Code Review Policy

## Purpose

この文書は、AtCoder用repositoryにおける独立code reviewの範囲、確認項目、finding形式を定める。Reviewはrepository保守の品質を確認するために行い、ユーザー本人の競技プログラミング能力を代替または補助するために使わない。

## README Authority

`README.md`は、ユーザーが最終化した公開方針の正本である。Reviewerは次をREADMEから判断し、README自体の書き換えを改善案にしない。

- Repositoryの目的は、個人の参加・練習記録と再利用libraryの保管であり、portfolioや模範解答集ではない。
- ディレクトリ構成はtext treeで示し、実際のtop-level directoryとの対応を保つ。
- `algorithm/`、`heuristic/`、`training/`は歴史的記録であり、正しさ、最適性、汎用性を保証しない。
- 継続的な保守対象は主に`mylib/`、`scripts/`、`snippets/`、`tests/`である。
- 解法codeは本人作成に限定し、第三者資料は本文やcodeを収録せず、必要に応じてURLだけを記録する。
- 生成AIの利用はrepository整備と許可されたlibrary保守に限定され、解法支援には使わない。
- Licenseを設定しないことと、複製・変更・再配布を一般許諾しないことは意図した公開条件である。

READMEと他のshared documentが競合する場合、ユーザーの最新の明示指示とREADMEを優先し、findingは従属文書側へ向ける。READMEの目的外であるportfolio品質、過去codeの一括改善、空の`heuristic/`への実装追加、file単位の一律なauthorship追記を要求しない。ディレクトリ構成のtext treeを表へ置き換えることも改善として提案しない。

## Review Preconditions

Review前に、次を確認する。

1. `README.md`に定めた目的、保守範囲、所有・出典、生成AI、公開条件。
2. Requirementとacceptance criteria。
3. Base commit、head commit、または対象diff。
4. Review対象file。
5. 実行済みのverificationと未確認領域。
6. 対象が`AGENTS.md`のAI Assistance Boundary内にあること。

開催中コンテストの問題文、code、error、実行結果、scoreを含む可能性がある場合は、fileを読まずにreviewを停止する。長期AHC等で公式規則上AIを利用できる場合も、ユーザーが当該コンテストでの利用範囲を明示するまでは対象外とする。

## Allowed Scope

- `README.md`、`AGENTS.md`、`CLAUDE.md`、`REVIEW.md`等のrepository文書。
- `.gitignore`、`pyproject.toml`等の設定とdependency管理。
- `scripts/`のrepository整備・生成処理。
- `snippets/`と`mylib/snippets.toml`の生成契約および同期。
- `tests/`のrepository layout、生成処理、許可されたlibrary保守に関するtest。
- ユーザーが明示的に依頼した、開催中コンテストと無関係な`mylib/`の保守、test、snippet連携。
- Directory移動、命名変更、生成物除外等の機械的なrepository整理。

## Excluded Scope

- `algorithm/`、`training/`、`heuristic/`にある解法codeの正誤、計算量、改善案、debug。
- 問題文の要約、着眼点、algorithm、data structure、証明、解法の提案。
- Contest成績やscoreへ直接影響する分析。
- 開催中コンテストに関する問題文、code、error、実行結果、score。
- Review対象外の過去提出codeを追加contextとして読むこと。

機械的な移動でこれらのpathがdiffに現れる場合、内容のsemantic reviewを行わず、rename検出、path、件数、layout test、生成物の混入だけを確認する。

## Review Dimensions

優先順位は次のとおり。

1. **AI boundary compliance**: AI利用禁止領域を読んだり、解法支援を行ったりしていないか。
2. **Requirement correctness**: 変更が依頼内容とacceptance criteriaを満たすか。
3. **Scope discipline**: 無関係な提出code、format、rename、refactorを混ぜていないか。
4. **Historical preservation**: 過去の提出・練習記録の内容を意図せず変えていないか。
5. **Source-of-truth consistency**: `mylib/`、`mylib/snippets.toml`、生成済みsnippetの責務が崩れていないか。
6. **Script correctness**: 生成・分割・検査scriptが入力を破壊せず、failureを正しく報告するか。
7. **Test adequacy**: 許可された変更のexpected behavior、boundary、failure behaviorをtestしているか。
8. **Configuration consistency**: Python version、dependency、Ruff、mypy、実行commandが一致するか。
9. **Repository hygiene**: 生成物、仮想環境、input、output、log、binaryがGit管理へ混入していないか。
10. **Documentation accuracy**: Directory責務、command、AI利用境界が実装と一致するか。

AI利用境界への違反は、実装の正しさに関係なく`BLOCKER`とする。

## Publication Readiness Review

このreviewは、repositoryの公開、visibility変更、public release、または第三者由来のcode、data、画像、文書、生成物を追加するときだけ実施する。通常のprivate開発へ毎回適用しない。

公開前reviewでも、`algorithm/`、`training/`、`heuristic/`の解法の正誤、計算量、改善方法を評価しない。対象fileの内容を解法支援へ使わず、次のprovenance metadataと公開境界だけを確認する。

1. Authorまたはprovider。
2. Source URL、取得日、version、取得方法。
3. 自作、本人の提出、解説からの再実装、第三者codeの転載・改変の区別。
4. License、利用規約、contest rule、attribution、再配布条件。
5. Current treeだけでなく、commit history、tag、release、Git LFSに公開不可fileが残っていないか。
6. Credential、個人情報、local path、非公開input／output／logが含まれないか。
7. Repository licenseと第三者assetの条件が両立するか。
8. `AGENTS.md`、`CLAUDE.md`、`REVIEW.md`、`.claude/settings.json`等のtracked Agent fileに、credential、個人path、private endpoint、過大なpermission、公開すべきでない運用情報が含まれないか。

Project共通の`AGENTS.md`、`CLAUDE.md`、`REVIEW.md`は公開対象として扱う。`CLAUDE.local.md`、`.claude/settings.local.json`、`.agent-handoff.md`はlocal-onlyであり、`.gitignore`によりcommitを防ぐ。Shared Agent fileを隠すことをsecurity boundaryにせず、permission、hook、CI、testによる強制を優先する。

AtCoder利用規約では、ユーザー自身が投稿したprogramの所有権と著作権は作成者に帰属する一方、ユーザー自身が作成したものを除くwebsite上の文章、画像、programその他のdataの権利はAtCoderまたは第三者に帰属するとされる。このため、本人の提出code、公式解説、他ユーザーのcodeを同じ条件で扱わない。

`_official`、`_evima`、`_user`、`_commentary`、`_original_author`等のfile名は、出典、authorship、再配布許可の証明ではない。解法を読まず、source記録と権利条件だけで次に分類する。

| 判定 | 公開時の扱い |
| --- | --- |
| Public-safe | 本人の著作物、または確認済みの条件を満たして公開できる。|
| Public-with-conditions | Attribution、NOTICE、license同梱等の条件を満たした場合だけ公開できる。|
| Reference-only | Source URLと由来だけを記録し、第三者asset本体はrepositoryへ含めない。|
| Blocked／unknown | Author、source、利用条件、再配布条件を確認できず、解消するまで公開対象に含めない。|

このrepositoryでは、公開対象をユーザー本人が作成したcodeと文書に限定する。第三者assetは、再配布可能なlicenseがある場合も原則として`Reference-only`とし、source URLだけを記録する。

Severityは次を基準とする。

- `BLOCKER`: Secret、個人情報、再配布禁止file、出典不明の第三者code、contest rule違反、公開不可fileのGit history残存。
- `MAJOR`: License compatibility、利用規約、attribution、history確認が不足し、公開可否を判断できない。
- `MINOR`: Source URL、取得日、version、citation等が不足しているが、authorshipと公開条件は確認済み。

Unknownを公開可能と推定しない。Reviewerは法的判断を保証せず、確認したevidence、未確認事項、必要な専門家判断を示す。公開の最終判断はユーザーが行う。

Repository-levelのownership申告は、それと矛盾するfile名、source記録、履歴、転載の痕跡等がない限り、本人作成を支えるevidenceとして扱う。本人作成と申告されたfileに一律のfile単位authorship記録を要求しない。生成AIの支援は、第三者codeの転載や外部licenseの混入とは別の事実であり、外部由来を示すevidenceがない状態で同一視しない。

Comment量、file size、更新頻度等のheuristicは確認候補の選定には使えるが、provenance違反やseverityの根拠には使わない。AI利用境界により内容を読まなかったfileや、時間・権限の制約で確認できなかった項目は、具体的な問題を示すevidenceがない限り`Areas not verified`へ記録し、findingや`Blocked／unknown`へ昇格させない。

READMEが明記するlicense未設定は、それ自体をfindingにしない。第三者asset、dependencyの再配布、または別文書のlicense表記と矛盾し、具体的な公開riskが生じる場合だけfindingとする。

## Finding Format

Observationは次の四種類に分ける。

| 種類 | 記録先 |
| --- | --- |
| 実際に検出したcontract違反またはfailure | Finding |
| Repository evidenceから具体的なfailure scenarioを示せるrisk | Finding |
| Review範囲外、未読、実行不能等により確認できなかった項目 | Areas not verified |
| 公開可否やcontract適合を左右しない改善案 | Notesまたはoptional recommendation |

「読んでいない」「確認していない」ことだけをProblemにしない。Findingには、現在のrepositoryで確認したevidenceと、そこから成立する具体的なfailure scenarioの両方を要求する。Userの最新の明示指示は一般的な文書規則より優先し、公開上のfailureがなければ文体等の運用差をpublication findingにしない。継続運用で迷いが生じる場合は、shared instructionへの例外追記を任意の改善として提案する。

各findingは次の形式で記載する。

- ID
- Severity: `BLOCKER`、`MAJOR`、`MINOR`
- Fileとline
- Category
- Problem
- Failure scenario
- Evidence
- Recommended direction
- Confidence

最後に次を記載する。

- Overall assessment
- Requirements examined
- Tests examined
- Areas not verified
- Remaining uncertainty

問題を確認できない場合、findingを作るための指摘を行わない。

## Review Artifact

Claude Codeは、findingがない場合も含め、完了したreviewを`.ai/reviews/current.md`へ保存する。独立性を保つため、repository、requirement、Git diff、test結果による分析が完了するまで、既存のreview artifactを読まない。

既存の`current.md`がある場合は、内容を判断材料にせず`.ai/reviews/archive/<YYYY-MM-DD-HHMM>.md`へ移してから新しい結果を書く。Artifactにはreview日時、base／headまたは対象diff、確認したrequirement・文書・test、summary、finding、未確認領域、残る不確実性を記録する。各findingには`Codex validation: UNREVIEWED`を付ける。

`.ai/reviews/`はlocal-onlyの一時成果物であり、Git管理しない。開催中contestの問題文、code、error、実行結果、score、credential、個人の絶対path、不要なcode全文を転記しない。Codexは各findingを検証し、`VALID`、`PARTIALLY_VALID`、`INVALID`、根拠、対応、verification、resolution commitをartifactへ追記する。恒久的な設計判断だけを共有文書、設定、testへ反映し、raw reviewを正本にしない。

## Verification

変更内容に応じて、該当するcommandだけを実行する。

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

`algorithm/`と`training/`へformatterを適用しない。Review対象外のcodeをtestする目的でAIへ入力しない。

## Handling Findings

Claude Codeのfindingは修正命令ではない。Codexは各findingをrepository evidenceとrequirementに照らして`VALID`、`PARTIALLY_VALID`、`INVALID`に分類し、成立する部分だけを最小変更で修正する。必要な場合はregression testを追加し、該当するverificationを再実行する。最終判断はユーザーが行う。

## References

- [AtCoder利用規約](https://atcoder.jp/tos?lang=ja)
- [Licensing a repository — GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [Removing sensitive data from a repository — GitHub Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [Licenses — Open Data Commons](https://opendatacommons.org/licenses/)
