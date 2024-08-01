from openai import OpenAI
from utils.config import GenerationConfig


def generate_text(prompt):
    config = GenerationConfig()
    client = OpenAI(
        base_url=config.base_url,
        api_key="token-abc123",
    )
    print(prompt)
    completion = client.chat.completions.create(
        model=config.model,
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content


def format_streaming_event(data):
    return f"data: {data}\n\n"


def generate_text_streaming(prompt):
    config = GenerationConfig()
    client = OpenAI(
        base_url=config.base_url,
        api_key="token-abc123",
    )

    completion = client.chat.completions.create(
        model=config.model,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for chunk in completion:
        yield format_streaming_event(chunk.choices[0].delta.content)
