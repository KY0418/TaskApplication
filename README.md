1.Python依存関係ファイルのセットアップ
 
 以下のコマンドでpyproject.tomlを作成

--poetry init

2.web環境の構築

2-1.webプロジェクトフォルダ内で以下のコマンドを実行し、必要なオプションを追加

--npm install vue@latest

2-2.必要なパッケージのインストール

--npm install pug-plugin

--npm install scss

--npm install unocss

3.コンテナのbuild

--docker compose build

4.データベースマイグレーション

--docker compose exec -it api python db_migrate_db

上記コマンドでマイグレーションが実行されない場合は、bashで以下のコマンドを実行

--python migrate_db.py

5.開発サーバの起動

--docker compose up


