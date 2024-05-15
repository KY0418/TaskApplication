1.Python依存関係ファイルのセットアップ
 
 以下のコマンドでpyproject.tomlを作成

-poetry init

2.web環境の構築

2-1.webプロジェクトフォルダ内で以下のコマンドを実行し、必要なオプションを追加

-npm install vue@latest

2-2.必要なパッケージのインストール

-npm install pug-plugin

-npm install scss

-npm install unocss

2.依存関係のインストール

-docker compose exec api poetry add uvicorn

-docker compose exec api poetry add fastapi

-docker compose exec api poetry add psycopg2

-docker compose exec api poetry add python-dotenv

3.データベースマイグレーション

-docker compose exec -it api python db_migrate_db

上記コマンドでマイグレーションが実行されない場合は、bashで以下のコマンドを実行

-python migrate_db.py

4.開発サーバの起動

-docker compose up


