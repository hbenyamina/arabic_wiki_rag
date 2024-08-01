import requests
from utils.config import EmbeddingConfig
import os


def embed_batch(text_batch):
    config = EmbeddingConfig()
    batch_size = config.batch_size
    headers = {"Content-Type": "application/json"}

    embeddings = []
    for i in range(0, len(text_batch), batch_size):
        batch = text_batch[i : i + batch_size]
        data = {"inputs": batch}

        response = requests.post(
            os.path.join(config.base_url, "embed"),
            headers=headers,
            json=data,
            timeout=10,
        )
        embedding = response.json()
        if isinstance(response.json(), list):
            embeddings.extend(embedding)
        else:
            print(embedding)
            raise AssertionError
    return [vector[: config.vector_size] for vector in embeddings]
