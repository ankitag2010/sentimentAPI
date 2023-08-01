from pydantic import BaseModel


class ResponseBody(BaseModel):
    sentiment: str
    probability: float
