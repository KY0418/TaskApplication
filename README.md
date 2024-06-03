1.Python依存関係ファイルのセットアップ
 
 以下のコマンドでpyproject.tomlを作成

- cd api
- poetry install

2.web環境の構築

webプロジェクトフォルダ内で以下のコマンドを実行し、必要なオプションを追加

- cd web
- npm install 

3.コンテナのbuild

- docker compose build

4.開発サーバの起動

- docker compose up

起動確認　
    web　http://localhost:3000
    api  http://localhost:8000

5.データベースマイグレーション

- docker compose exec -it api python db_migrate_db

上記コマンドでマイグレーションが実行されない場合は、bashで以下のコマンドを実行

- python migrate_db.py


