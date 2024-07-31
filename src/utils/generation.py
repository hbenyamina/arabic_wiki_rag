from openai import OpenAI
from utils.config import GenerationConfig


def generate_text(prompt):
    config = GenerationConfig()
    client = OpenAI(
        base_url=config.base_url,
        api_key="token-abc123",
    )

    completion = client.chat.completions.create(
        model=config.model,
        messages=[{"role": "user", "content": prompt}],
    )
