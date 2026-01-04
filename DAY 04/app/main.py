from fastapi import FastAPI

app = FastAPI()

#Path parameter
@app.get("/user_id/{user_id}")
async def get_user_id(user_id: int):
    return {"user_id": user_id}

#Query Parameter
@app.get("/search")
async def get_result(q: str = None):
    return {"result": f"Search for {q}"}
