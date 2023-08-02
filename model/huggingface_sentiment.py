from transformers import pipeline
from model.requestBody import RequestBody
from model.responseBody import ResponseBody

def get_sentiment(requestBody: RequestBody):
    sentiment_pipeline = pipeline("sentiment-analysis")
    output = sentiment_pipeline(requestBody.sentence)
    print(output)
    return ResponseBody(sentiment=output[0]['label'], probability=output[0]['score'])