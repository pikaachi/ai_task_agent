from fastapi import FastAPI
from app.routers import tasks

app = FastAPI()

app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Task Agent API!"}