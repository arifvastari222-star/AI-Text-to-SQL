from ai.sql_generator import generate_sql
from database.query_executor import execute_query

question = "Delete all customers"

from utils.sql_validator import validate_sql

sql = generate_sql(question)

validate_sql(sql)

print(repr(sql))

print("\nGenerated SQL:")
print(sql)

df = execute_query(sql)

print("\nResults:")
print(df)