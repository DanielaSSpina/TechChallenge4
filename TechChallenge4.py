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

# Gerenciar o estado da página selecionada
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = 'Introdução'  # Página inicial

# Funções para selecionar a página
def select_page(page_name):
    st.session_state.selected_page = page_name

# Criar botões para as páginas
for page_name in pages.keys():
    if st.button(page_name):
        select_page(page_name)

# Carregar a página selecionada
pages = pages[st.session_state.selected_page]
pages.app()
