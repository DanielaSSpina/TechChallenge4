import streamlit as st
from Pages.Home import app as home_app
from Pages.About import app as about_app

st.title('Tech Challenge 4 | Fiapp')

# Dicionário com as páginas
pages = {
    "Introdução": Introdução_app,
    "Metodologia": Metodologia_app,
    "Análise": Análise_app,
    "Previsão": Previsão_app,
    "Referências": Referências_app,
}

# Menu lateral de navegação
st.sidebar.title("Menu")
selection = st.sidebar.radio("Ir para", list(pages.keys()))

# Carregar a página selecionada
page = pages[selection]
page()
