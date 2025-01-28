from openai import OpenAI
from . import secret_manager

def initialize_openai_client():
    OPENAI_API_KEY = secret_manager.get_openai_secret()
    openai_client = OpenAI(api_key=OPENAI_API_KEY)
    return openai_client

def test():
    chatgpt = initialize_openai_client()
    res = chatgpt.chat.completions.create(
        model = 'gpt-4o',
        messages = [
            {'role': 'system', "content": "You are a greeting bot"},
            {'role': 'user', "content": "You have to communicate with users by Japanese anytime"},
        ]
    )
    return res.choices[0].message

def chat(text: str):
    chatgpt = initialize_openai_client()
    res = chatgpt.chat.completions.create(
        model = 'gpt-4o',
        messages = [
            {'role': 'system', "content": "ユーザからの入力を元に適切な返答をしてください"},
            {'role': 'user', "content": f"{text}"},
        ]
    )
    return res.choices[0].message
