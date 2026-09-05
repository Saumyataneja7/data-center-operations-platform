from ai.sql_generator import generate_sql

sql = generate_sql(
    "Show top 5 servers having lowest health score."
)

print(sql)