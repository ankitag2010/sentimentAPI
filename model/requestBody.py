
from pydantic import BaseModel


class RequestBody(BaseModel):
    sentence: str
