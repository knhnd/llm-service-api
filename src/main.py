from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .services.chatgpt import ChatGPT

app = FastAPI()

# Avoid CORS Error
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World!"}

@app.get("/chatgpt/test/{text}")
async def chatgpt_test(text: str):
    res = ChatGPT.test(text) 
    return res.content
