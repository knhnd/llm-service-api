# LLM Service API

`ChatGPT` や `Gemini` など大規模言語モデルに関連するサービスの API を実行するための Web API

- `Secret Manager` を利用した安全なアクセス制御
- `Python` の Web Framework である [FastAPI](https://fastapi.tiangolo.com/ja/) を用いて実装

## Server

### Local

- `main.py` のある階層（`src/`）で `uvicorn main:app --reload`

### Docker

プロジェクトルートに `Dockerfile`, `docker-compose.yml`, `dockerignore`, `requirements.txt` を作成

- `docker-compose build`
- `docker-compose up -d`
- `docker-compose stop`

## [Google Cloud](https://cloud.google.com/?hl=ja)

### [Cloud Run](https://cloud.google.com/run?hl=ja) (Deploy)

- セットアップ
    - `gcloud components update` で `gcloud CLI` をアップデート
    - `gcloud auth login` (ログインしていなければ)
    - `gcloud config set project PROJECT_ID`
        - `PROJECT_ID` は [Google Cloud]((https://cloud.google.com/?hl=ja)) のプロジェクトダッシュボードから確認
- デプロイの実行
    - `gcloud run deploy`
        - 質問項目はすべてそのまま Enter or Yes で問題ない
        - リージョンは `[2] asia-east1`
        - コンテナのビルドとデプロイが完了し `URL` が払い出されれば OK

`API Key` は Google Cloud の Secret Manager で管理

### [Service Account](https://cloud.google.com/iam/docs/service-account-overview?hl=ja)

- サービスアカウントを新規作成
    - サービスアカウント名を設定
    - ロールを `Secret Manager Secret Accessor` に設定
    - ③ のサービスアカウント自体のアクセス制御はスキップして完了
    - 鍵を追加 > 新しい鍵を作成 > `JSON`
        - `JSON` ファイルが自動でダウンロードされるので厳重に保管

### [Secret Manager](https://cloud.google.com/secret-manager?hl=ja)

- シークレットの新規作成
    - 作成したサービスアカウントの`JSON`ファイルをインポートするか内容をコピペ
    - 他の設定はそのままで「シークレットを作成」で完了


### [Cloud Run でシークレットを使用](https://cloud.google.com/run/docs/configuring/secrets?hl=ja)

- CloudRun のコンソールを開く
- 新しいリビジョンの編集とデプロイ
    - 「セキュリティ」タブ
        - サービスアカウントを作成したものに変更
    - 「コンテナ」タブ > コンテナ > 変数とシークレット
        - 「シークレットを参照」
            - 環境変数名を設定
            - 作成したシークレットを指定

## LLM Services

### [OpenAI](https://platform.openai.com/docs/overview)

- `API Key` の作成
    - 任意の権限を設定
    - `API Key` の文字列は作成時に一度しか確認できないのですぐに Google の Secret Manager に登録
    - 参考：[Best Practices for API Key Safety](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)

### [Gemini](https://gemini.google.com/)

未対応

## Reference

- [CloudRun & Docker 入門](https://zenn.dev/kenken82/articles/cloudrun-docker-tutorial)
- [OpenAI APIキーを安全に使用するためのベストプラクティス](https://note.com/komzweb/n/n3392c290d7b8)
