import sqlglot
from sqlglot import expressions


def validate_sql(sql):

    try:

        parsed = sqlglot.parse_one(
            sql,
            dialect="postgres"
        )

        if not isinstance(parsed, expressions.Select):
            return False, "Only SELECT queries are allowed."

        return True, "SQL is valid."

    except Exception as e:

        return False, f"Invalid SQL: {e}"