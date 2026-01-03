from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"msg": "Welcome to First FastAPI Project"}


@app.get("/users")
def get_users():
    return {"users": ["Rahul", "Krishna", "Bhajan"]}


@app.post("/users")
def create_user():
    return {"msg": "Users Created"}
