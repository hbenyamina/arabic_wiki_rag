from utils.data_models import History
from utils.milvus import get_client, semantic_search
from utils.embedding import embed_batch
from utils.generation import generate_text
from typing import List


def generate_response(query, history: List[History]):
    vector = embed_batch(["query: " + query])
    client = get_client()
    documents = semantic_search(client, vector)
    context = [document["text"] for document in documents]
    prompt = """Given the following context, answer the quesion: {{question}}
    Context:
    {{context}}
    """.format(
        question=query, context=context
    )
    generate_text(prompt)
