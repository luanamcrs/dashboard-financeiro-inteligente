import pandas as pd
from sqlalchemy import text

from database.connection import engine


def get_transactions() -> pd.DataFrame:
    query = """
        SELECT *
        FROM transactions
    """

    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)

    return df


def get_total_spent(df: pd.DataFrame) -> float:
    return df["valor"].sum()


def get_top_category(df: pd.DataFrame):
    grouped = (
        df.groupby("categoria")["valor"]
        .sum()
        .sort_values(ascending=False)
    )

    return grouped.index[0], grouped.iloc[0]


def get_expenses_by_category(df: pd.DataFrame):
    return (
        df.groupby("categoria")["valor"]
        .sum()
        .sort_values(ascending=False)
    )


def get_top_expenses(df: pd.DataFrame, top_n=5):
    return (
        df.sort_values("valor", ascending=False)
        .head(top_n)
    )