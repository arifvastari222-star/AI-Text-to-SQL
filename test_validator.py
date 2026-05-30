from utils.sql_validator import validate_sql

sql = "DELETE FROM customers"

validate_sql(sql)

print("Passed")