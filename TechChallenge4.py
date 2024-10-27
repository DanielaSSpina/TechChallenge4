import streamlit as st
from pages.Introdução import app as Introdução_app
from pages.Metodologia import app as Metodologia_app
from pages.Análise import app as Análise_app
from pages.Previsão import app as Previsão_app
from pages.Referências import app as Referências_app

st.title('Tech Challenge 4 | Fiapp')

# Dicionário com as páginas
pages = {
    "Introdução": Introdução_app,
    "Metodologia": Metodologia_app,
    "Análise": Análise_app,
    "Previsão": Previsão_app,
    "Referências": Referências_app
}

# Menu de navegação na parte principal
selection = st.radio("Ir para", list(pages.keys()))

# Carregar a página selecionada
page = pages[selection]
page()
