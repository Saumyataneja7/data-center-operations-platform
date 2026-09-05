from db import execute_query

def execute_generated_sql(sql_query: str):
    return execute_query(sql_query)