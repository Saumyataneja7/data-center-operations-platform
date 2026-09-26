# Data Center AI Copilot

Streamlit AI Copilot for natural-language data-center operations analysis.

## Public portfolio deployment

The public demo runs in **Demo Mode** using a small local SQLite dataset derived from the project's telemetry data. This keeps the portfolio demo independent of an Azure subscription while preserving the production architecture.

Set these Streamlit secrets:

```toml
GEMINI_API_KEY = "your-key"
DEMO_MODE = "true"
```

For a live Azure/Databricks deployment, set `DEMO_MODE = "false"` and provide the three Databricks credentials.

## Run locally

```bash
cd DataCenter_AI
pip install -r requirements.txt
streamlit run app.py
```
