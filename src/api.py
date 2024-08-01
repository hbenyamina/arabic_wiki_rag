from pydantic import BaseModel, Field
from typing import List
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from utils.data_models import History
from rag import generate_response,generate_response_streaming
import uvicorn

app = FastAPI()


class SearchModel(BaseModel):
    query: str
    history: List[History] = Field(None)


@app.get("/ask")
def search_endpoint(request: SearchModel):
    return generate_response(request.query, request.history)


@app.get("/ask/stream")
async def stream_endpoint(request: SearchModel):
    return StreamingResponse(
        generate_response_streaming(request.query, request.history),
        media_type="text/event-stream",
    )


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
