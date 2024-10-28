import streamlit as st
from pages.Introdução import app as Introdução_app
from pages.Metodologia import app as Metodologia_app
from pages.Análise import app as Análise_app
from pages.Previsão import app as Previsão_app
from pages.Referências import app as Referências_app

st.title('Tech Challenge 4 | Fiapp')
st.subheader('teste')

# Dicionário com as páginas
pages = {
    "Introdução": Introdução_app,
    "Metodologia": Metodologia_app,
    "Análise": Análise_app,
    "Previsão": Previsão_app,
    "Referências": Referências_app
}

# Inicializa a variável para a página atual
current_page = None

# Criar botões em colunas
col_count = len(pages)
cols = st.columns(col_count)

# Criar botões para as páginas
for i, page_name in enumerate(pages.keys()):
    with cols[i]:
        if st.button(page_name):
            current_page = page_name  # Define a página atual

# Carregar a página selecionada
if current_page:
    page = pages[current_page]
    page()  # Chama a função 'app()' da página selecionada
else:
    st.write("Por favor, selecione uma página.")
