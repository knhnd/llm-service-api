# LLM API

大規模言語モデルを安全に利用するための Web API

## About

`ChatGPT` や `Gemini` など大規模言語モデルに関連するアプリケーションの API を安全に実行するための Web API．
`Secret Manager` などを利用してキー情報を守るため LLM サービスへのアクセスにはこの Web API を経由する．

## 実装

`Python` の Web Framework である [FastAPI](https://fastapi.tiangolo.com/ja/) を用いて実装．

### Local Server

- `main.py` のある階層で `uvicorn main:app --reload`

## Google Cloud

- [コンソール](https://console.cloud.google.com/welcome?_ga=2.238480646.-726073305.1718693528&hl=ja&authuser=1&project=llm-api-429208)

### Secret Manager

### Deploy: Cloud Run

## Links

- [OpenAI API](https://platform.openai.com/docs/overview)
- [Google AI for Developers (Gemini)](https://ai.google.dev/)

---