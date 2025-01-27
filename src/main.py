from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .libs import chatgpt

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

@app.get("/chatgpt")
async def chatgpt_test():
    res = chatgpt.test() 
    return res.content

@app.get("/chatgpt/chat/{text}")
async def chatgpt_chat(text: str):
    res = chatgpt.chat(text) 
    return res.content