import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    GOOGLE_AI_API_KEY = os.getenv("GOOGLE_AI_API_KEY ","")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY","")
    COHERE_API_KEY = os.getenv("COHERA_API_KEY","")
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY","")