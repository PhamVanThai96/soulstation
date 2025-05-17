# sk-181966568c8142eabec0b0a992315b36
## pip install chat-deepseek-api python-dotenv


import asyncio
import os
from deepseek_api import DeepseekAPI
from dotenv import load_dotenv

load_dotenv()

async def translate_text():
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set DEEPSEEK_API_KEY in your .env file.")

    client = DeepseekAPI(api_key=api_key)

    prompt = "Translate the following English sentence into Vietnamese: 'This is a sample sentence about physics.'"

    response = await client.chat(prompt)
    print("Bản dịch:", response)

if __name__ == "__main__":
    asyncio.run(translate_text())
