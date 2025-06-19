from fastapi import APIRouter
from pydantic import BaseModel

# from src.inference import run_prompt


router = APIRouter()


class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 128  # Optional override


def run_prompt(prompt: str, max_tokens: int):
    return f"prompt: {prompt}\nmax_tokens: {max_tokens}"


@router.post("/")
async def infer(req: PromptRequest):
    output = run_prompt(req.prompt, req.max_tokens)
    return {"response": output}
