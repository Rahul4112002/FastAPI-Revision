from fastapi import FastAPI

app = FastAPI()


@app.get("/sync-users")
def sync_users():
    return {"Sync Users": ["Rahul","Krishna","Bhajan"]}


@app.get("/async-users")
async def async_usrs():
    return {"Async Users": ["Chetna", "Shomi", "Isha"]}


