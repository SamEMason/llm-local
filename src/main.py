from fastapi import FastAPI
from src.config import load_config
from src.routes import router


config = load_config()
app = FastAPI()

app.include_router(router=router, prefix=config["api"]["endpoint"])


@app.get("/")
async def test_endpoint():
    env = config.get("env", "undefined")
    return {"message": f"Running in {env} mode"}
