from dotenv import load_dotenv
from pathlib import Path
import os
import streamlit as st

# Local development: load .env if present.
load_dotenv(Path(__file__).parent / ".env")

def _secret_or_env(name: str, default=None):
    try:
        value = st.secrets.get(name)
        if value not in (None, ""):
            return value
    except Exception:
        pass
    return os.getenv(name, default)

DATABRICKS_SERVER_HOSTNAME = _secret_or_env("DATABRICKS_SERVER_HOSTNAME")
DATABRICKS_HTTP_PATH = _secret_or_env("DATABRICKS_HTTP_PATH")
DATABRICKS_TOKEN = _secret_or_env("DATABRICKS_TOKEN")
GEMINI_API_KEY = _secret_or_env("GEMINI_API_KEY")

DEMO_MODE = str(_secret_or_env("DEMO_MODE", "true")).lower() in {"1", "true", "yes", "on"}
