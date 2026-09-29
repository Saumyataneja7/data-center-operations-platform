def validate_sql(sql: str):

    print("========== SQL VALIDATOR DEBUG ==========")
    print("RAW SQL:", repr(sql))
    print("STARTS SELECT:", sql.strip().upper().startswith("SELECT"))
    print("STARTS WITH:", sql.strip().upper().startswith("WITH"))
    print("=========================================")

    return True
