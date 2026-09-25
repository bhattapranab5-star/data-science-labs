import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise RuntimeError("DATABASE_URL was not found in .env")

engine = create_engine(database_url)

with engine.connect() as connection:
    result = connection.execute(
        text(
            """
            SELECT
                current_database() AS database_name,
                current_user AS user_name,
                NOW() AS current_time;
            """
        )
    )

    row = result.mappings().one()
    print(dict(row))

df = pd.read_sql(
    """
    SELECT
        current_database() AS database_name,
        current_user AS user_name,
        NOW() AS current_time;
    """,
    engine,
)

print()
print(df)