# A dataimport os
from dataclasses import dataclass
import os


@dataclass
class GenerationConfig:
    model: str = os.getenv("GENERATION_MODEL", "CohereForAI/aya-23-8B")
    base_url: str = os.getenv("GENERATION_SERVER_BASE_URL", "http://127.0.0.1:8000/v1")


@dataclass
class EmbeddingConfig:
    model: str = os.getenv("EMBEDDING_MODEL", "intfloat/multilingual-e5-base")
    base_url: str = os.getenv("EMBEDDING_SERVER_BASE_URL", "http://127.0.0.1:8080")
    batch_size: int = os.getenv("EMBEDDING_BATCH_SIZE", 16)


@dataclass
class MilvusConfig:
    uri: str = os.getenv("MILVUS_CLIENT_URI", "http://localhost:19530")
