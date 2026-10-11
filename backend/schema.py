from sqlalchemy import inspect

from backend.database import engine


def get_database_schema():

    inspector = inspect(engine)

    schema = {}

    for table_name in inspector.get_table_names():

        columns = inspector.get_columns(table_name)

        schema[table_name] = []

        for column in columns:

            schema[table_name].append({
                "name": column["name"],
                "type": str(column["type"])
            })

    return schema