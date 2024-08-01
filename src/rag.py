from utils.data_models import History
from utils.milvus import get_client, semantic_search
from utils.embedding import embed_batch
from utils.generation import generate_text, generate_text_streaming
from utils.prompts import SYSTEM_RAG_PROMPT, USER_RAG_PROMPT
from typing import List


def generate_response(query, history: List[History]):
    vector = embed_batch(["query: " + query])
    client = get_client()
    documents = semantic_search(client, vector)[0]
    context = [document["entity"]["text"] for document in documents]
    if history:
        conversation_history = "\n".join(
            [f"Question: {h.question}\nAnswer: {h.answer}" for h in history]
        )
    else:
        conversation_history = ""
    user_prompt = USER_RAG_PROMPT.format(
        question=query, context=context, conversation_history=conversation_history
    )
    return generate_text(SYSTEM_RAG_PROMPT, user_prompt)


def generate_response_streaming(query, history: List[History]):
    vector = embed_batch(["query: " + query])
    client = get_client()
    documents = semantic_search(client, vector)[0]
    context = [document["entity"]["text"] for document in documents]
    if history:
        conversation_history = "\n".join(
            [f"Question: {h.question}\nAnswer: {h.answer}" for h in history]
        )
    else:
        conversation_history = ""
    user_prompt = USER_RAG_PROMPT.format(
        question=query, context=context, conversation_history=conversation_history
    )
    return generate_text_streaming(SYSTEM_RAG_PROMPT, user_prompt)
