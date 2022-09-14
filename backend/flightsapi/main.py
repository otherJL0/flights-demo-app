import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello world"}


def main():
    uvicorn.run("flightsapi.main:app", host="127.0.0.1", port=5000, log_level="info")
