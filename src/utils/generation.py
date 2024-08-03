from openai import OpenAI
from utils.config import GenerationConfig

DUMMY_TOKEN = "token-abc123"


def generate_text(system_prompt, user_prompt):
    config = GenerationConfig()
    client = OpenAI(
        base_url=config.base_url,
        api_key=DUMMY_TOKEN,
    )
    completion = client.chat.completions.create(
        model=config.model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=config.temperature,
    )
    return completion.choices[0].message.content


def generate_text_streaming(system_prompt, user_prompt):
    config = GenerationConfig()
    client = OpenAI(
        base_url=config.base_url,
        api_key=DUMMY_TOKEN,
    )

    completion = client.chat.completions.create(
        model=config.model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        stream=True,
        temperature=config.temperature,
    )
    for chunk in completion:
        chunk_text = chunk.choices[0].delta.content
        if chunk_text:
            yield chunk_text
