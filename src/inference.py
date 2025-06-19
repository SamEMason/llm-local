from llama_cpp import Llama
from src.config import load_config
from typing import TypedDict, List, cast


config = load_config()


class CompletionChoice(TypedDict):
    text: str


class CompletionResponse(TypedDict):
    choices: List[CompletionChoice]


llm = Llama(
    model_path=config["model"]["path"],
    n_ctx=config["model"]["context_size"],
    n_threads=config["model"]["threads"],
)


def run_prompt(prompt: str, max_tokens: int) -> str:
    raw = llm(prompt, max_tokens=max_tokens, stream=False)
    output = cast(CompletionResponse, raw)
    return output["choices"][0]["text"].strip()
