
from http.client import HTTPException
from typing import List
from fastapi import FastAPI
from pydantic.v1.main import Model

app = FastAPI()
students_m = []

@app.get("/hello", status_code=200)
def dire_hello():
    return "hello world"

@app.get ("/welcome", status_code=200)
def welcome_name(request: app):
    return  {f"welcome {request.name}"}

class Student(Model):
    Reference: str
    FisrtName: str
    LastName: str
    Age: int

    @app.post("/students")
def add_students(students: List[Student], students_m=None):
    students_m.extend(students)
    return students_m


@app.get("/students", status_code=200)
def object_students():
    return students_m

@app.get("/students-authorized")
def students_authorized(authorization=None, none=None):
    if authorization is none:
        raise HTTPException(status_code=401, detail="unauthorized")
    if authorization != "bon courage":
        raise HTTPException(status_code=403, detail="Forbidden")