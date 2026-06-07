import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:

    # Converter coluna data
    df["data"] = pd.to_datetime(df["data"])

    # Remover espaços extras
    df["descricao"] = df["descricao"].str.strip()
    df["categoria"] = df["categoria"].str.strip()

    # Padronizar categoria
    df["categoria"] = df["categoria"].str.title()

    # Remover linhas duplicadas
    df = df.drop_duplicates()

    # Remover valores negativos
    df = df[df["valor"] > 0]

    return df