from fastapi import FastAPI
from config.config import settings
from app.routers.root import router as root_router
from app.routers.openai import router as openai_router

app = FastAPI(title="FastAPI OpenAI Agent Test")

app.include_router(root_router)
app.include_router(openai_router)
