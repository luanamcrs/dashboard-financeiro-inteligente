import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import streamlit as st
import pandas as pd

from etl.transform import transform_data
from etl.load import load_data

st.title("📂 Upload de Dados")

uploaded_file = st.file_uploader(
    "Selecione um arquivo CSV",
    type=["csv"]
)

if uploaded_file is not None:

    try:

        df = pd.read_csv(uploaded_file)

        st.subheader("Pré-visualização")

        st.dataframe(df.head())

        if st.button("Processar Arquivo"):

            df = transform_data(df)

            load_data(df)

            st.success(
                f"{len(df)} registros carregados com sucesso!"
            )

    except Exception as e:

        st.error(f"Erro ao processar arquivo: {e}")

# Exemplo de Arquivo a ser enviado
example_df = pd.DataFrame({
    "data": [
        "2026-06-01",
        "2026-06-02",
        "2026-06-03"
    ],
    "descricao": [
        "Supermercado",
        "Netflix",
        "Uber"
    ],
    "categoria": [
        "Alimentacao",
        "Assinaturas",
        "Transporte"
    ],
    "valor": [
        250.50,
        39.90,
        28.75
    ]
})

st.subheader("📋 Exemplo de Arquivo")

st.dataframe(
    example_df,
    use_container_width=True
)

# Modelo de Arquivo
csv = example_df.to_csv(index=False)

st.download_button(
    label="⬇️ Baixar Modelo CSV",
    data=csv,
    file_name="modelo_gastos.csv",
    mime="text/csv"
)