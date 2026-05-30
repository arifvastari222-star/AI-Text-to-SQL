from sql_generator import generate_sql

question = "Show top 5 states by customer count"

sql = generate_sql(question)

print(sql)