from gemini import ask_gemini

from ai.prompt_builder import build_sql_prompt
from ai.sql_validator import validate_sql


def generate_sql(question):

    prompt = build_sql_prompt(question)

    sql = ask_gemini(prompt)

    # Remove markdown code fences
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    # Extract the actual SQL statement if Gemini adds explanation
    select_pos = sql.upper().find("SELECT")
    with_pos = sql.upper().find("WITH")

    positions = [p for p in (select_pos, with_pos) if p >= 0]

    if not positions:
        raise Exception("Gemini did not return a valid SQL query.")

    sql = sql[min(positions):].strip()

    # Remove trailing semicolon
    sql = sql.rstrip(";").strip()

    # Validate SQL before execution
    validate_sql(sql)

    return sql
