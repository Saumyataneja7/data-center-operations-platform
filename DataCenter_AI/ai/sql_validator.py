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
    "REVOKE"
]


def validate_sql(sql: str):

    sql_upper = sql.upper().strip()

    # Allow only SELECT queries
    if not sql_upper.startswith("SELECT"):
        raise Exception("Only SELECT queries are allowed.")

    # Block dangerous SQL
    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in sql_upper:
            raise Exception(f"Unsafe SQL detected: {keyword}")

    return True
