import re

FORBIDDEN_KEYWORDS = {
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "TRUNCATE",
    "MERGE",
    "CREATE",
    "GRANT",
    "REVOKE",
}


def validate_sql(sql: str):

    sql_upper = sql.upper().strip().rstrip(";").strip()

    # Only SELECT or CTE-based SELECT statements
    if not (sql_upper.startswith("SELECT") or sql_upper.startswith("WITH")):
        raise Exception("Only SELECT queries are allowed.")

    # Detect forbidden SQL keywords as whole words
    for keyword in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{keyword}\b", sql_upper):
            raise Exception(f"Unsafe SQL detected: {keyword}")

    return True
