from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette.requests import Request
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "GET utilisé"}


@app.post("/")
def create_item():
    return {"message": "POST utilisé"}

@app.put("/")
def update_item():
    return {"message": "PUT utilisé"}

@app.delete("/")
def delete_item():
    return {"message": "DELETE utilisé"}

@app.patch("/")
def patch_item():
    return {"message": "PATCH utilisé"}