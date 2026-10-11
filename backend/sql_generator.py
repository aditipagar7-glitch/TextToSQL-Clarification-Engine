from backend.llm import ask_llm
from backend.schema import get_database_schema


def generate_sql(question):

    schema = get_database_schema()

    prompt = f"""
You are an expert PostgreSQL SQL generator.

Your job is to convert the user's natural language question
into a PostgreSQL SELECT query.

DATABASE SCHEMA:

{schema}

USER QUESTION:

{question}

RULES:

1. Generate only SELECT queries.
2. Do not generate INSERT.
3. Do not generate UPDATE.
4. Do not generate DELETE.
5. Do not generate DROP.
6. Do not generate ALTER.
7. Use only tables and columns present in the schema.
8. Use correct JOIN conditions.
9. Do not explain the SQL.
10. Return only the SQL query.

SQL:
"""

    response = ask_llm(prompt)

    return response.strip()