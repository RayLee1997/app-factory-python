from openai import OpenAI
from config.config import settings

client = OpenAI(api_key=settings.openai_api_key)

async def get_completion(prompt: str, max_tokens: int = 5) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )
    return response.choices[0].message.content.strip() if response.choices else ""
