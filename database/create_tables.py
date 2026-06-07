from pathlib import Path
from sqlalchemy import text

from connection import engine

schema_path = Path("database/schema.sql")

with open(schema_path, "r", encoding="utf-8") as file:
    sql_script = file.read()

with engine.connect() as conn:
    conn.execute(text(sql_script))
    conn.commit()

print("Tabela criada com sucesso!")