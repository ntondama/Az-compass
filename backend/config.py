from dotenv import load_dotenv
import os

load_dotenv()

AZURE_AI_PROJECT_ENDPOINT = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
MODEL_NAME = os.getenv("AZURE_OPENAI_MODEL", "gpt-4.1")
DATA_FOLDER = os.getenv("DATA_FOLDER", "data")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
