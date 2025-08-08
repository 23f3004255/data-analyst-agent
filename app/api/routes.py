from fastapi import APIRouter, File, UploadFile
from app.services.dispatcher import handle_request

router = APIRouter()

@router.post("/")
async def analyze(
    questions: UploadFile = File(...),
    files: list[UploadFile] = File(None)
):
    return await handle_request(questions, files)