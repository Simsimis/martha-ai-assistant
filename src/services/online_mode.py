# Handles interaction with cloud AIs (GPT, Gemini, etc.).
import requests
from src.config import OPENAI_API_KEY


def get_online_response(text):
    """
    Sends the user's text to the online LLM (e.g., OpenAI GPT-4) and returns the response.
    This function sets up the system prompt and handles the API call.
    """
    # Example: Call OpenAI's Chat API (pseudo-code)
    system_prompt = "You are Martha, a sarcastic, snarky AI assistant inspired by Karen from SpongeBob."
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    }
    # TODO: Replace with actual API endpoint and error handling
    # response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    # return response.json()["choices"][0]["message"]["content"]
    pass  # Placeholder for actual API call
