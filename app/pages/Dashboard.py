import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import streamlit as st
import plotly.express as px

from services.analytics import (
    get_transactions,
    get_total_spent,
    get_top_category,
    get_category_summary,
    get_top_expenses
)

st.title("📊 Dashboard Financeiro")

df = get_transactions()

# Filtros
st.sidebar.header("🔎 Filtros")

categorias = sorted(df["categoria"].unique())

categoria_selecionada = st.sidebar.multiselect(
    "Categoria",
    categorias,
    default=categorias
)

data_inicial = st.sidebar.date_input(
    "Data Inicial",
    value=df["data"].min()
)

data_final = st.sidebar.date_input(
    "Data Final",
    value=df["data"].max()
)

df = df[
    df["categoria"].isin(categoria_selecionada)
]

df = df[
    (df["data"].dt.date >= data_inicial)
    &
    (df["data"].dt.date <= data_final)
]

# Evitar Erros
if df.empty:
    st.warning(
        "Nenhum registro encontrado para os filtros selecionados."
    )
    st.stop()

total_gasto = get_total_spent(df)
categoria, valor_categoria = get_top_category(df)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "💸 Total Gasto",
        f"R$ {total_gasto:,.2f}"
    )

with col2:
    st.metric(
        "🏆 Maior Categoria",
        categoria
    )

st.divider()

category_df = get_category_summary(df)

fig = px.pie(
    category_df,
    names="categoria",
    values="valor",
    title="Distribuição dos Gastos"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

fig_bar = px.bar(
    category_df,
    x="categoria",
    y="valor",
    text_auto=".2f",
    title="Gastos por Categoria"
)

st.plotly_chart(
    fig_bar,
    use_container_width=True
)

st.divider()

st.subheader("🏆 Top 5 Despesas")

st.dataframe(
    get_top_expenses(df),
    use_container_width=True
)