from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
  name: str
  age : int
  email: str
  is_active: bool
  
@app.post("/users")
async def create_users(user: User):
  return {"msg":"User is Created", "data": user}
  