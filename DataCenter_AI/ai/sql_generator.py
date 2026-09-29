from gemini import ask_gemini

from ai.prompt_builder import build_sql_prompt
from ai.sql_validator import validate_sql


def generate_sql(question):

    prompt = build_sql_prompt(question)

    sql = ask_gemini(prompt)

    print("========== GEMINI RAW RESPONSE ==========")
    print(repr(sql))
    print("=========================================")

    # Remove markdown fences
    sql = sql.replace("```sql", "")
    sql = sql.replace("```SQL", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    # Find the beginning of the SQL statement
    select_pos = sql.upper().find("SELECT")
    with_pos = sql.upper().find("WITH")

    positions = [p for p in (select_pos, with_pos) if p >= 0]

    if not positions:
        raise Exception(
            f"Gemini returned an unexpected response: {repr(sql[:500])}"
        )

    sql = sql[min(positions):].strip()

    validate_sql(sql)

    return sql
