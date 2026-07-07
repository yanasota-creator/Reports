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

## 自動化ルール
- 実験フォルダ内の data/（例：experiment-1-strain-gauge/data/）に新しいCSVが追加されたら、ルートのSTYLE_GUIDE.mdのルールに沿って、その実験のレポート（.md）を生成する
- 生成したレポートは、対応する実験フォルダの中に保存する
- 新しい実験フォルダを作成したら、ルートのINDEX.mdに1行追記する
- pushする際は、pre-pushフックが表示する警告（STYLE_GUIDE.mdやINDEX.mdの変更時）を確認し、必要であればClaude.aiのReportsプロジェクトの知識ファイルも更新するようユーザーに促す
