from fastapi import FastAPI
from app.routes.when import router as WhenRouter


app = FastAPI()

app.include_router(WhenRouter, tags=["Reading"],prefix="/reading")

@app.get("/")
async def root():
    return {"message": "Welcome to the Bible Verses for your Feelings!"}