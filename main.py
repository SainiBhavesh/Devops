from fastapi import FastAPI

from function import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
    "http://localhost",
    "http://localhost:8000"
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/src={src}&dest={dest}')
def generate(src:str,dest:str):
    x=submit(src.lower(),dest.lower())
    return x
    