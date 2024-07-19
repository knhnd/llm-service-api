from openai import OpenAI
from .secret_manager import Secret_Manager

class ChatGPT:
    OPENAI_API_KEY = Secret_Manager.get_openai_api_key()
    openai_client = OpenAI(api_key=OPENAI_API_KEY)

    def test(text):
        res = ChatGPT.openai_client.chat.completions.create(
            model = 'gpt-3.5-turbo',
            messages = [
                {'role': 'system', "content": "You are a Greeting Bot"},
                {'role': 'user', "content": "You have to communicate with users by Japanese"},
            ]
        )
        return res.choices[0].message
