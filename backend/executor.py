import pandas as pd
from sqlalchemy import text

from backend.database import engine


def execute_sql(sql):

    with engine.connect() as connection:

        result = connection.execute(text(sql))

        rows = result.fetchall()

        columns = result.keys()

        return pd.DataFrame(
            rows,
            columns=columns
        )