from pydantic import BaseModel


class History(BaseModel):
    question: str
    answer: str
