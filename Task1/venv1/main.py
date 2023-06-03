from fastapi import FastAPI

import logging

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

@app.post("/add")
async def add(x: int, y: int):
    result = x + y
    return {"result": result}



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("this is the frist task in MLOops course!")