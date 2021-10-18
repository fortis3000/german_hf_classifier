from fastapi import FastAPI

from config_logging import logger
from src.data_models import Sentence
from src.model import model

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello!"}


@app.get("/health")
async def health():
    return {"message": "Server is OK."}


@app.post("/predict")
async def predict(query: Sentence):
    logger.info(f"Message received: {query.text}")
    return {
        "message": "OK",
        "received": query.text,
        "score": model.predict_sentiment([query.text])[0],
    }
