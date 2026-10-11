from backend.schema import get_database_schema

schema = get_database_schema()

for table, columns in schema.items():

    print("\nTABLE:", table)

    for column in columns:
        print(
            " ",
            column["name"],
            "->",
            column["type"]
        )