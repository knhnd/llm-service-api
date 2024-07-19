import os
from dotenv import load_dotenv
from google.cloud import secretmanager

class Secret_Manager:
    # Service Account を取得
    # service_account_key = os.environ["service_account_key.json"]  # local でのテスト用
    service_account_key = os.environ["cloudrun-dev"]
    client = secretmanager.SecretManagerServiceClient.from_service_account_json(service_account_key)
    
    def get_openai_api_key():
        # load_dotenv()  # local
        PROJECT_ID = os.environ["PROJECT_ID"]
        SECRET_ID = os.environ["SECRET_ID"]
        VERSION = os.environ["VERSION"]
        # OpenAI API Key の取得
        path = Secret_Manager.client.secret_version_path(PROJECT_ID, SECRET_ID, VERSION)
        response = Secret_Manager.client.access_secret_version(name=path)
        secret_value = response.payload.data.decode('UTF-8')
        return secret_value
