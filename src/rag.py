from utils.data_models import History
from utils.milvus import get_client, semantic_search
from utils.embedding import embed_batch
from utils.generation import generate_text, generate_text_streaming
from typing import List


def generate_response(query, history: List[History]):
    vector = embed_batch(["query: " + query])
    client = get_client()
    documents = semantic_search(client, vector)[0]
    print(documents)
    context = [document["entity"]["text"] for document in documents]
    prompt = """Given the following context, answer the quesion: {question}
    Context:
    {context}
    You must answer in Arabic.
    """.format(
        question=query, context=context
    )
    return generate_text(prompt)


def generate_response_streaming(query, history: List[History]):
    vector = embed_batch(["query: " + query])
    client = get_client()
    documents = semantic_search(client, vector)[0]
    context = [document["entity"]["text"] for document in documents]
    prompt = """Given the following context, answer the quesion: {question}
    Context:
    {context}
    You must answer in Arabic.
    """.format(
        question=query, context=context
    )
    return generate_text_streaming(prompt)
