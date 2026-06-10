from groq import GroqClient
from dotenv import load_dotenv
import os
from src.prompts import prompter

load_dotenv()

class GroqLLMClient:
    def __init__(self):
        self.client = GroqClient(api_key = os.getenv("GROQ_API_KEY"))
        
    def generate(self, prompt):
        response = self.client.generate(
            model="llama-3.3-70b-versatile",
            prompt=prompter.prompt(prompt['stock_name'], prompt['articles_text']),
            max_tokens=100,
            temperature=0.7,
        )
        return response.text