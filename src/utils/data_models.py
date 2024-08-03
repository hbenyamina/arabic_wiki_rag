from pydantic import BaseModel, Field
from typing import List


class History(BaseModel):
    question: str
    answer: str


class SearchModel(BaseModel):
    query: str
    history: List[History] = Field(None)
