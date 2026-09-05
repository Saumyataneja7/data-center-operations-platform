from gemini import ask_gemini

from ai.prompt_builder import build_sql_prompt
from ai.sql_validator import validate_sql


def generate_sql(question):

    prompt = build_sql_prompt(question)

    sql = ask_gemini(prompt)

    # Remove markdown if Gemini returns it
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    # Validate SQL before execution
    validate_sql(sql)

    return sql