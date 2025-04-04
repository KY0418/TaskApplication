1.Python 依存関係ファイルのセットアップ

以下のコマンドで python のパッケージをインストール

- cd api
- poetry install

Python の version は 3.11 以上に設定する

2.web 環境の構築

web プロジェクトフォルダ内で以下のコマンドを実行後に、必要なオプションを追加

- cd web
- npm install

  3.コンテナの build

- ./scripts/dev.sh build もしくは ./scripts/dev.sh build --no-cache

  4.開発サーバの起動

- ./scripts/dev.sh up

起動確認　
web http://localhost:3000
api http://localhost:8000

5.migrate database

- docker compose exec task_be poetry run python -m migrations.migrate_db --trigger
