from ai.sql_generator import generate_sql
from ai.sql_executor import execute_generated_sql
from ai.answer_generator import generate_answer

question = "Show top 5 servers having lowest health score."

sql = generate_sql(question)

print("\nGenerated SQL:\n")
print(sql)

df = execute_generated_sql(sql)

print("\nReturned Data:\n")
print(df)

answer = generate_answer(question, df)

print("\nAI Summary:\n")
print(answer)