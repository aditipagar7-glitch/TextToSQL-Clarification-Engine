from backend.sql_generator import generate_sql


question = "Show all customers from Pune"

sql = generate_sql(question)

print(sql)