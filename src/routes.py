from fastapi import APIRouter
from pydantic import BaseModel
from src.inference import run_prompt
from typing import Dict


router = APIRouter()


class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 128  # Optional override


@router.post("/", response_model=Dict[str, str])
async def infer(req: PromptRequest):
    output = run_prompt(req.prompt, req.max_tokens)
    return {"response": output}
