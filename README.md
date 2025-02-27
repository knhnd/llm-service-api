# LLM Service API

大規模言語モデルの `API` を実行するための `Web API`

- `Python` の Web Framework である [FastAPI](https://fastapi.tiangolo.com/ja/) を用いて実装
- `Secret Manager` を利用した安全なアクセス制御

### Local Server

- `main.py` のある階層（`src`）で `uvicorn main:app --reload`

### Docker

プロジェクトルートに `Dockerfile`, `docker-compose.yml`, `dockerignore`, `requirements.txt` を作成。`requirements.txt` のライブラリのバージョンは確認を忘れないようにする。

- `Docker Desktop` アプリを起動
- `docker-compose build`
- `docker-compose up -d`
- `docker-compose stop`

## LLM Services

### [OpenAI](https://platform.openai.com/docs/overview)

- `API Key` の作成
  - 任意の権限を設定
  - `API Key` の文字列は作成時に一度しか確認できないのですぐに Google の Secret Manager に登録
    - 参考：[Best Practices for API Key Safety](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)

## Deploy

### [Cloud Run](https://cloud.google.com/run?hl=ja)

コンテナ化して `Cloud Run` にデプロイ

- Service URL: https://llm-service-api-600033825441.asia-east1.run.app
- [Dashboard](https://console.cloud.google.com/run?hl=ja&inv=1&invt=Abn-qQ&project=llm-service-442200&supportedpurview=project,organizationId,folder)

#### セットアップ

- `gcloud components update` で `gcloud CLI` をアップデート
- ログインしていなければ `gcloud auth login`
- `gcloud config set project PROJECT_ID`
  - `PROJECT_ID` は [Google Cloud](<(https://cloud.google.com/?hl=ja)>) のプロジェクトダッシュボードから確認
- デプロイの実行
  - `gcloud run deploy`
    - 質問項目はすべてそのまま Enter or Yes で問題ない
    - リージョンは `[2] asia-east1`
    - コンテナのビルドとデプロイが完了し `URL` が払い出されれば OK

## Google Cloud

- [コンソール (LLM Service)](https://console.cloud.google.com/home/dashboard?hl=ja&inv=1&invt=Abn-cg&project=llm-service-442200&supportedpurview=project,organizationId,folder)

1. Cloud Run にデプロイしたアプリを実行するための「サービスアカウント」を作成
2. OpenAI API などの API Key は Secret Manager に保存
3. Cloud Run の環境変数にサービスアカウントを作成したプロジェクトIDとシークレットのID(openai-api-keyなど)を設定
4. エンドポイントにリクエストしてアプリが実行され LLM の機能を実行し、レスポンスが返ってくるかを確認

### [Service Account](https://cloud.google.com/iam/docs/service-account-overview?hl=ja)

- サービスアカウントの新規作成
  - Google Cloud のダッシュボードで「`IAMと管理 > サービスアカウント`」にアクセス
  - サービスアカウントの作成
    - サービスアカウント名を設定
  - ロールを `Secret Manager Secret Accessor` に設定
    - ③ のサービスアカウント自体のアクセス制御はスキップして完了
  - キー > 鍵を追加 > 新しい鍵を作成 > `JSON`
    - `JSON` ファイルが自動でダウンロードされるので厳重に保管
      - GitHub に push されないように注意

### [Secret Manager](https://cloud.google.com/secret-manager?hl=ja)

- シークレットの新規作成
  - Google Cloud のダッシュボードで「`セキュリティ > Secret Manager`」にアクセス
  - シークレットを作成
  - 利用するサービスのアクセストークンや `API Key` を登録
  - 他の設定はそのままで「シークレットを作成」で完了

### [Cloud Run でシークレットを使用](https://cloud.google.com/run/docs/configuring/secrets?hl=ja)

- [シークレットの取得](https://cloud.google.com/secret-manager/docs/samples/secretmanager-get-secret?hl=ja#secretmanager_get_secret-python)

- CloudRun のコンソールを開く
- 新しいリビジョンの編集とデプロイ
  - 「セキュリティ」タブ
    - サービスアカウントを作成したものに変更
  - 「コンテナ」タブ > コンテナ > 変数とシークレット
    - 利用するシークレットの `PROJECT_ID`, `SECRET_ID`, `VERSION` を環境変数に登録
  - 「コンテナ」タブ > コンテナ > ボリュームのマウント
    - 登録したシークレットを指定
    - マウントパスは任意のものを指定
- ここまで設定したらアプリからシークレットにアクセスするためのコードを書く
  - `./src/libs/secret_manager.py`

#### アクセス制御

サービスアカウント、シークレットマネージャ、LLM の API Key それぞれで権限が設定できるので組み合わせてアクセスを制限する。

## Reference

- [CloudRun & Docker 入門](https://zenn.dev/kenken82/articles/cloudrun-docker-tutorial)
- [OpenAI API キーを安全に使用するためのベストプラクティス](https://note.com/komzweb/n/n3392c290d7b8)
