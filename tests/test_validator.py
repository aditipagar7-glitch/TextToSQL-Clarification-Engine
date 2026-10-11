from backend.validator import validate_sql

sql = "SELECT * FROM customers"

valid, message = validate_sql(sql)

print(valid)
print(message)