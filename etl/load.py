import pandas as pd

from database.connection import engine


def load_data(df: pd.DataFrame):

    df.to_sql(
        name="transactions",
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"{len(df)} registros carregados com sucesso!")