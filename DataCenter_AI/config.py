from dotenv import load_dotenv
from pathlib import Path
import os

# Load .env from the same folder as config.py
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

DATABRICKS_SERVER_HOSTNAME = os.getenv("DATABRICKS_SERVER_HOSTNAME")
DATABRICKS_HTTP_PATH = os.getenv("DATABRICKS_HTTP_PATH")
DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")