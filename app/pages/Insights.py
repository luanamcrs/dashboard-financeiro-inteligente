import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import streamlit as st

from services.analytics import (
    get_transactions,
    get_total_spent,
    get_top_category,
    get_top_expenses
)

st.title("Insights Financeiros")

df = get_transactions()

total = get_total_spent(df)

categoria, valor_categoria = get_top_category(df)

percentual = (valor_categoria / total) * 100

maior_despesa = get_top_expenses(df, 1)

st.info(
    f"Você gastou {percentual:.1f}% do total em {categoria}."
)

st.success(
    f"Sua maior despesa foi '{maior_despesa.iloc[0]['descricao']}' "
    f"no valor de R$ {maior_despesa.iloc[0]['valor']:.2f}."
)

st.subheader("Resumo Financeiro")

st.write(f"Total gasto: R$ {total:.2f}")

st.write(f"Categoria com maior gasto: {categoria}")