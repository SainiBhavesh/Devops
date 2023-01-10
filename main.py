from fastapi import FastAPI
from function import *

app=FastAPI()

@app.get('/src={src}&dest={dest}')
def generate(src:str,dest:str):
    submit(src,dest)
    return ""