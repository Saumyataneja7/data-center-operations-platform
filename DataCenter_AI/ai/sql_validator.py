FORBIDDEN_KEYWORDS = [
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
]


def validate_sql(sql: str):

    sql_upper = sql.upper().strip()

    # Remove a trailing semicolon if Gemini adds one
    sql_upper = sql_upper.rstrip(";").strip()

    # Only SELECT statements and CTE-based SELECT statements are allowed
    if not (sql_upper.startswith("SELECT") or sql_upper.startswith("WITH")):
        raise Exception("Only SELECT queries are allowed.")

    # Block dangerous SQL keywords
    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in sql_upper:
            raise Exception(f"Unsafe SQL detected: {keyword}")

    return True
