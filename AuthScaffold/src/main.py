from typing import Union
from fastapi import FastAPI


app = FastAPI()

app.get("/")
async def root():
    """
    don't use this root endpoint
    """
    return {"message": ""}