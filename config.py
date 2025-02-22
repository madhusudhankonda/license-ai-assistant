import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key with error handling
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please check your .env file.") 