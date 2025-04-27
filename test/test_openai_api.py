from openai import OpenAI
import pytest
from config.config import settings

import logging
from config.logging_config import init_logging

init_logging()
logger = logging.getLogger(__name__)

client = OpenAI(api_key=settings.openai_api_key)


def test_openai_api_key_present():
    # Ensure the API key is loaded from environment
    print(f"OPENAI_API_KEY: {settings.openai_api_key}")

    assert settings.openai_api_key, "OPENAI_API_KEY is not set in environment"

    logger.info("OPENAI_API_KEY loaded: %s", settings.openai_api_key)


def test_openai_completion():
    # Test that OpenAI completion endpoint is reachable and returns a non-empty response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello, world!"}],
        max_tokens=5,
    )
    assert hasattr(response, "choices"), "Response missing 'choices'"
    assert response.choices, "No choices returned by OpenAI"
    text = response.choices[0].message.content.strip()
    assert text, "OpenAI returned empty text"
    logger.info("OpenAI returned text: %s", text)
    print(f"OpenAI response: {text}")
