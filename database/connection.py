from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "SUA_SENHA"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"
DB_NAME = "dashboard-financeiro"

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)