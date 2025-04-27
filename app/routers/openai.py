from fastapi import APIRouter
from app.services.openai_service import get_completion

router = APIRouter()

@router.get("/openai-test")
async def openai_test():
    text = await get_completion("Hello, world!")
    return {"response": text}
