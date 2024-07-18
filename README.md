# LLM Service API

大規模言語モデルのサービスを安全に利用するための Web API

## About

`ChatGPT` や `Gemini` など大規模言語モデルに関連するアプリケーションの API を安全に実行するための Web API．
`Secret Manager` などを利用してキー情報を守るため LLM サービスへのアクセスには Webhook でこの Web API を経由する．

## 実装

`Python` の Web Framework である [FastAPI](https://fastapi.tiangolo.com/ja/) を用いて実装．

### Local Server

- `main.py` のある階層で `uvicorn main:app --reload`

## Google Cloud

- [コンソール](https://console.cloud.google.com/welcome?_ga=2.238480646.-726073305.1718693528&hl=ja&authuser=1&project=llm-api-429208)

### Deploy: Cloud Run


### Secret Manager

- [サービスアカウント](https://console.cloud.google.com/iam-admin/serviceaccounts?referrer=search&authuser=1&hl=ja&project=llm-api-429208)
- [シークレットマネージャ](https://console.cloud.google.com/security/secret-manager/secret/chatgpt-admin/versions?authuser=1&hl=ja&project=llm-api-429208)

#### Usage

`.env` に Secret Manager に登録した `Secret` の情報を記載し、`service_account_key.json`　で指定したサービスアカウントで Secret Manager からキーを取得

- Google Cloud にアクセス
- サービスアカウントを作成
    - `service_account_key.json` をダウンロード
        - プロジェクトルートに設置
        - `.gitignore` に追記
- 各種サービスで `API_KEY` を発行（今回は ChatGPT）
- `API_KEY` を Secret Manager に登録
- ローカルに `.env` を作成し、Secret の `PROJECT_ID`、`SECRET_ID`、`VERSION` を記載
    - `.gitignore` に追記
- `service_account_key.json` を利用して Secret Manager から API キーを取得
    - コードを実行して API キーが取得できればOK

## LLM Services

### ChatGPT

- [OpenAI Dashboard](https://platform.openai.com/playground/chat?models=gpt-4o)

#### API_KEY

[Best Practices for API Key Safety](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety) を参考にして利用

- `API_KEY` の文字列は作成時に一度表示されるだけで以降は表示できない
    - 作成時にコピーして Google の Secret Manager に登録しておく 

## Links

- [OpenAI API](https://platform.openai.com/docs/overview)
    - [OpenAI developer documentation](https://platform.openai.com/docs/overview)
    - [Best Practices for API Key Safety](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)
- [Google AI for Developers (Gemini)](https://ai.google.dev/)

---