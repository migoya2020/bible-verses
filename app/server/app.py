from fastapi import FastAPI
from app.routes.when import router as WhenRouter


app = FastAPI()

app.include_router(WhenRouter, tags=["When"],prefix="/when")

@app.get("/")
async def root():
    return {"message": "Hellow World"}