import os
from dotenv import load_dotenv
from google.cloud import secretmanager
from google.oauth2 import service_account

load_dotenv()

PROJECT_ID = os.environ["PROJECT_ID"]
SECRET_ID = os.environ["SECRET_ID"]
VERSION = os.environ["VERSION"]

key_path = './../service_account_key.json'
client = secretmanager.SecretManagerServiceClient.from_service_account_json(key_path)

path = client.secret_version_path(PROJECT_ID, SECRET_ID, VERSION)

response = client.access_secret_version(name=path)
secret_value = response.payload.data.decode('UTF-8')

print(secret_value)