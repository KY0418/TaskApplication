1.Python 依存関係ファイルのセットアップ

以下のコマンドで pyproject.toml を作成

- cd api
- poetry install

Python の version は 3.11 以上に設定する

2.web 環境の構築

web プロジェクトフォルダ内で以下のコマンドを実行し、必要なオプションを追加

- cd web
- npm install

  3.コンテナの build

- docker compose build

  4.開発サーバの起動

- docker compose up

起動確認　
web 　 http://localhost:3000
api http://localhost:8000

5.データベースマイグレーション

- docker compose exec api poetry run python -m migrate_db

上記コマンドでマイグレーションが実行されない場合は、bash で以下のコマンドを実行

- python migrate_db.py

マイグレーション完了後は db.init の項番 1,2 の SQL を実行する
