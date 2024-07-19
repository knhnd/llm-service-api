import os
from dotenv import load_dotenv
from google.cloud import secretmanager

class Secret_Manager:    
    def get_secret():
        # 環境変数の取得
        # load_dotenv()  # local
        PROJECT_ID = os.environ["PROJECT_ID"]
        SECRET_ID = os.environ["SECRET_ID"]
        VERSION = os.environ["VERSION"]
        # シークレット（API Key）の取得
        client = secretmanager.SecretManagerServiceClient()
        path = client.secret_version_path(PROJECT_ID, SECRET_ID, VERSION)
        response = client.access_secret_version(name=path)
        secret_value = response.payload.data.decode('UTF-8')
        return secret_value
