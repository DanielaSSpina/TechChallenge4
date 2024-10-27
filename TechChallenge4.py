import streamlit as st
from pages.Introdução import app as Introdução_app
from pages.Metodologia import app as Metodologia_app
from pages.Análise import app as Análise_app
from pages.Previsão import app as Previsão_app
from pages.Referências import app as Referências_app

# Título da aplicação
st.title('Tech Challenge 4 | Fiapp')

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

# Criar botões para as páginas
for page_name in pages.keys():
    if st.button(page_name):  # Cria um botão para cada página
        current_page = page_name  # Define a página atual como a página do botão clicado

# Carregar a página selecionada
if current_page:
    page = pages[current_page]
    page()  # Chama a função 'app()' da página selecionada
else:
    # Carrega uma página padrão se nenhum botão for clicado
    st.write("Por favor, selecione uma página.")
