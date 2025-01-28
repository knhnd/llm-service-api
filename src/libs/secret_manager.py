import os
from google.cloud import secretmanager

def get_openai_secret():
    # 環境変数の読み込み
    PROJECT_ID = os.environ["PROJECT_ID"]
    SECRET_ID = os.environ["SECRET"]
    VERSION = os.environ["VERSION"]

    # シークレットマネージャから API Key を取得
    client = secretmanager.SecretManagerServiceClient()
    path = client.secret_version_path(PROJECT_ID, SECRET_ID, VERSION)
    response = client.access_secret_version(name=path)
    secret_value = response.payload.data.decode('UTF-8')
    return secret_value
