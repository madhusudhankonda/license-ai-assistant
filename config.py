import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenRouter configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables. Please check your .env file.")

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Available models
AVAILABLE_MODELS = {
    "Gemini Flash 2.0": "google/gemini-2.0-flash-001",
    "GPT-4o": "openai/gpt-4o",
    "GPT-4o-mini": "openai/gpt-4o-mini",
    "Anthropic Claude 3.5 Sonnet": "anthropic/claude-3.5-sonnet",
    "Anthropic Claude 3.5 Haiku": "anthropic/claude-3.5-haiku",
    "Mistral 24B": "mistralai/mistral-small-24b-instruct-2501:free",
    "Llama 3.1 8B": "meta-llama/Llama-3.1-8B-Instruct"
}

# Default model
DEFAULT_MODEL = AVAILABLE_MODELS["GPT-4o"] 