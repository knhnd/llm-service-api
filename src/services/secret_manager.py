import os
from dotenv import load_dotenv
from google.cloud import secretmanager

class Secret_Manager:

    # ローカルでテスト
    def get_openai_api_key_test():
        load_dotenv()
        # Secret Manager のアクセス情報を取得
        PROJECT_ID = os.environ["PROJECT_ID"]
        SECRET_ID = os.environ["SECRET_ID"]
        VERSION = os.environ["VERSION"]
        # Service Account 情報を取得
        service_account_key = os.environ["SERVICE_ACCOUNT"]
        client = secretmanager.SecretManagerServiceClient.from_service_account_json(service_account_key)
        
        # シークレットの取得
        path = client.secret_version_path(PROJECT_ID, SECRET_ID, VERSION)
        response = client.access_secret_version(name=path)
        secret_value = response.payload.data.decode('UTF-8')
        return secret_value