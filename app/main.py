import streamlit as st

st.set_page_config(
    page_title="Dashboard Financeiro Inteligente",
    layout="wide"
)

st.title("🏠 Dashboard Financeiro Inteligente")

st.markdown("""
### Bem-vindo!

Este projeto foi desenvolvido para demonstrar competências em:

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- ETL
- Streamlit
- Plotly
- Data Analytics
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Tecnologias", "7+")

with col2:
    st.metric("Banco de Dados", "PostgreSQL")

with col3:
    st.metric("Visualização", "Plotly")

st.info(
    "Utilize o menu lateral para navegar entre Dashboard, Insights e Upload de Dados."
)