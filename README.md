# Engineering-Reports

工学実験レポート置き場．実験ごとのフォルダ構成・リンク一覧は [INDEX.md](INDEX.md) を参照．

## Gitフックのセットアップ

`.git/hooks/` はリポジトリ管理外（cloneしても引き継がれない）のため、新しい環境ではリポジトリ内の `scripts/hooks/` から手動でコピーする．

```sh
cp scripts/hooks/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-push
```

- `pre-push`：pushしようとするコミットに `STYLE_GUIDE.md` または `INDEX.md` の変更が含まれる場合、「Claude.aiのReportsプロジェクトの知識ファイルも更新すること」という警告を表示する（push自体は止めない）。
