from transformers import pipeline
from model.requestBody import RequestBody
from model.responseBody import ResponseBody

def get_sentiment(requestBody: RequestBody):
    sentiment_pipeline = pipeline("sentiment-analysis")
    data = ["I love you", "I hate you"]
    output = sentiment_pipeline(requestBody.sentence)
    return ResponseBody(sentiment=output.label, probability=output.score)