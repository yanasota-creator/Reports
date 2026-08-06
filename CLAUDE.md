# CLAUDE.md について

このファイルは、Claude Codeがこのフォルダ（Reports）で作業する際に、
起動するたびに自動的に読み込む設定ファイルです。

ここに書かれたルールに従うことで、「data/にCSV追加したのでレポート作って」のような
簡単な一言の指示だけで、Claude Codeが正しい手順（STYLE_GUIDEに沿った作成、保存先、
INDEX.mdの更新など）を自動的に踏まえて作業できるようになります。

## リポジトリの構成説明
- ルートのINDEX.md：全実験への目次（一覧のみ）
- 各実験フォルダ（例：experiment-1-strain-gauge）内のINDEX.md：その実験のデータ・画像への詳細リンク一覧
- ルートのSTYLE_GUIDE.md・pdf_style.css：レポート執筆の共通ルールとPDF用スタイル（全実験で共通）
- scripts/hooks/pre-push：pre-pushフックのバックアップ（新環境では .git/hooks/ に手動コピーが必要）

## 権限について

- Claude Codeには、このリポジトリ（Reportsフォルダ以下）以外のフォルダ・ファイルを削除する権限を与えない
- ダウンロードフォルダ等、リポジトリ外のファイルを参照・コピーするのは良いが、削除や上書きはしない
- リポジトリとダウンロードフォルダ以外の場所を探索する必要がある場合は、自動実行モードであっても必ず事前にユーザーに確認を取る

## 自動化ルール
- 実験フォルダ内の data/（例：experiment-1-strain-gauge/data/）に新しいCSVが追加されたら、ルートのSTYLE_GUIDE.mdのルールに沿って、その実験のレポート（.md）を生成する
- 生成したレポートは、対応する実験フォルダの中に保存する
- 新しい実験フォルダを作成したら、ルートのINDEX.mdに1行追記する
- pushする際は、pre-pushフックが表示する警告（STYLE_GUIDE.md・INDEX.md・CLAUDE.mdの変更時）を確認し、必要であればClaude.aiのReportsプロジェクトの知識ファイルも更新するようユーザーに促す
- レポート（.md）を生成・修正した後は、`grep -n '\\\[' report.md`（実際のファイル名に置き換える）を実行し、参考文献の引用箇所にバックスラッシュ（\[ \]）が誤って混入していないか確認する。混入していた場合は`<sup>[1]</sup>`の形に修正する。

## トラブルシューティング：ファイルが正しく読み込めない時

「バイナリと判定される」「文字化けする」など、原因不明のエラーが出た場合は、以下の順で切り分ける：

1. GitHub側の認識を確認：curl -sI <raw URLアドレス> でcontent-typeを確認
2. OS側の判定を確認：file -i <ファイル名> で種類・文字コードを確認
3. 文字コードの厳密検証：iconv -f UTF-8 -t UTF-8 <ファイル名> -o /dev/null でエラーの有無を確認
4. 先頭バイトの目視確認：head -c 3 <ファイル名> | xxd でBOM等の混入を確認

これらが全て「正常」を示す場合、原因はファイルではなくClaude側の読み取りツールの癖である可能性が高い。その場合は、チャットへの直接アップロードなど、別の読み込み経路に切り替える。

## トラブルシューティング：PDFに体裁（字下げ・明朝体・ページ番号）が反映されない時

「エクスポートし直したのに見た目が変わらない」場合は、推測せずPDFそのものを解析して切り分ける。ユーザーの画面は見えないので、出来上がったPDFが唯一の証拠になる。

### 1. まずPDFを解析して「どこまで効いているか」を確定させる

```sh
ls -l --time-style=full-iso report.pdf          # そもそも再出力されているか
pdfinfo report.pdf | grep -E "Creator|CreationDate"   # 出力エンジン・出力時刻
pdffonts report.pdf | awk 'NR>2{print $1}' | sort -u  # 実際に埋め込まれたフォント
pdftotext -layout report.pdf - | grep -nE '^\s*[0-9]+(/[0-9]+)?\s*$'  # ページ番号の形式
pdftoppm -png -r 100 -f 1 -l 1 report.pdf <出力先>/p   # 画像化して目視（字下げの有無等）
```

- 本文が明朝体か：フォント名で判定する（`Meiryo`・`Noto-Sans-JP`＝ゴシック、`Noto-Serif-JP`・`Yu Mincho`＝明朝）
- **どのフォントがどこで使われているか**は`pdftohtml -xml -stdout report.pdf`で`<fontspec>`のidと`<text font="...">`を突き合わせる。「一部だけ効いている」状況の判別に有効

### 2. 「一部だけ効く」時はCSSの詳細度を疑う

Markdown PDF拡張は内蔵CSSで`body`にsans-serifを指定している。`pdf_style.css`側で`body`や`p`に素で書くと負けるため、セレクタを重ねて`!important`を付ける（`.katex ...`のような詳細度の高い指定だけ効いている、という症状が出たらこれ）。

### 3. 「全く効かない」時は設定の読み込み経路を疑う

設定は次の2か所にあり、**実際にどちらが効いているか**を確認する（STYLE_GUIDE.md 11章参照）。

- ワークスペース設定：`Reports/.vscode/settings.json`（**Reportsフォルダをフォルダとして開いている時だけ**有効）
- ユーザー設定：`/mnt/c/Users/<ユーザー名>/AppData/Roaming/Code/User/settings.json`（Windows側でVSCodeを動かしている場合）

判定方法：ユーザーに`Ctrl+,`→`markdown-pdf.footerTemplate`を検索→「ワークスペース」タブの値を見てもらう。拡張の初期値（`… / <span class='totalPages'></span>`を含む形）が出ていれば、ワークスペース設定は読まれていない。

### 4. 過去の実績（2026/8/6）

**症状**：CSSの一部（KaTeX関連）だけ効き、本文フォント・字下げ・ページ番号が変わらない。

**真因**：ユーザー設定の`markdown-pdf.styles`が`C:\Users\...\Documents\GitHub\pdf_style.css`という**既に存在しないパス**を指していた。リポジトリをWindows側からWSL側（`~/projects/Reports`）へ移した際に更新し忘れたもの。「前回までは効いていた」という証言はこの型の典型的なサインなので、**設定値が指すパスの実在を必ず確認する**。あわせて`stylesRelativePathFile`が`true`だと相対パスがmdファイル基準になる点にも注意（ワークスペース基準にしたい場合は`false`）。

なお、`/mnt/c`以下（リポジトリ外）を読み書きする場合は、自動実行モードであっても事前にユーザーの許可を取り、変更前にバックアップを取る。
