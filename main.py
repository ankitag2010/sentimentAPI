


import sys
sys.path.append('/app/app/')
from fastapi import FastAPI
from model.requestBody import RequestBody
from model.huggingface_sentiment import get_sentiment

app = FastAPI()


@app.post("/sentiment/")
async def getSentiment(request: RequestBody):
    return get_sentiment(request)
