from gemini import ask_gemini

from ai.prompt_builder import build_sql_prompt
from ai.sql_validator import validate_sql


def generate_sql(question):

    prompt = build_sql_prompt(question)

    sql = ask_gemini(prompt)

    # Temporary debugging
    print("========== GEMINI RAW RESPONSE ==========")
    print(repr(sql))
    print("=========================================")

    # Remove markdown fences
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    print("========== CLEANED SQL ==========")
    print(repr(sql))
    print("=================================")

    validate_sql(sql)

    return sql
