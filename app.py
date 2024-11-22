import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuração do título do aplicativo
st.set_page_config(page_title="Projeto de Previsão de Preço de Petróleo", page_icon="📊", layout="wide")

st.markdown("<p style='font-size:40px; color:#B40C40;'>Tech Challenge 4 | Fiap</p>", unsafe_allow_html=True)

# Criando um menu de navegação com `selectbox` ou `radio`
pagina = st.sidebar.radio("Escolha a Página", ["Introdução", "Metodologia", "Principais Acontecimentos", 
                                               "Dashboard Interativo", "MVP", "Conclusão", "Referências"])

# Conteúdo de cada página
if pagina == "Introdução":
    st.markdown("<h3 style='color:#264CAC;'>Introdução</h3>", unsafe_allow_html=True)
    st.write('''Este trabalho tem como foco apresentar a análise do preço do petróleo brent, trazendo quatro acontecimentos que auxiliem a explicação das variação do preço e podem variar desde fatores geopolíticos até avanços tecnológicos. 
Traremos além dos acontecimentos, uma análise por meio de um dashboard dinâmico dos dados, previsão analisada e MVP.''')

    st.markdown("<h3 style='color:#264CAC;'>Ferramentas utilizadas</h3>", unsafe_allow_html=True)
    st.write('Para a realização deste trabalho, foi utilizado as seguintes ferramentas:')
    st.write('Python: utilizado para toda a tratativa inicial das bases como organização das colunas, remoção de espaços e duplicidades e valores nulo, assim como para a realização da previsão dos preços do petróleo por meio do modelo de machine learning PROPHET.')
    st.write('PowerBI: utilizado para a criação de um dashboard interativo compilando as informações disponíveis do preço do petróleo, previsão e acontecimentos que influenciam na explicação da variação do preço.')
    st.write('Streamlit: utilizado para desenvolvimento do MVP (Minimum Viable Product, ou Produto Mínimo Viável) e disponibilização das etapas e informações do projeto.')

elif pagina == "Metodologia":
    st.markdown("<h3 style='color:#264CAC;'>Metodologia</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#6C778A;'>Origem e análise dos dados</h3>", unsafe_allow_html=True)
    st.write('Os dados utilizados nesta análise foram extraídos do site do Instituto de Pesquisa Econômica Aplicada (Ipea). Após a extração, os dados foram salvos em um arquivo csv, e importados no python para tratamentos iniciais mostrados abaixo:')
    st. image ('Imagens/Phyton/Pyhton - importanto bibliotecas.png', caption='importando e instalando bibliotecas necessárias')
    st.image('Imagens/Phyton/Pyhton - tratamento dos dados.png', caption='importação da base de dados e tratamento inicial')

    st.markdown("<h3 style='color:#6C778A;'>Modelo de Machine Learning</h3>", unsafe_allow_html=True)
    st.write('Para realizar o machine learning dos nossos dados, utilizamos o modelo Prophet, pois é uma ferramenta que se destaca em cenários onde previsões de longo prazo e ajustes a tendências e sazonalidades complexas são necessários.')
    st. image ('Imagens/Phyton/Python - preparação dados previsão.png', caption='preparando os dados para o Prophet')
    st. image ('Imagens/Phyton/Python - preparação dados previsão 2.png', caption='visualizando datas e df')
    st. image ('Imagens/Phyton/Python - preparação dados previsão 3.png', caption='ajustando dados data e criando index')
    st. image ('Imagens/Phyton/Python - preparação dados previsão 4.png', caption='iniciando a previsão dos dados')
    st. image ('Imagens/Phyton/Python - Plot Prophet.png', caption='gráficos plotados de tendência e sazonalidade')
    st. image ('Imagens/Phyton/Python - Forecast.png', caption='criação do forecast')
    st. image ('Imagens/Phyton/Python - criando arquivo de previsão.png', caption='criando arquivo de previsão')
    st. image ('Imagens/Phyton/Python - acurácia dados previsão.png', caption='validando acurácia do modelo')

elif pagina == "Principais Acontecimentos":
    st.markdown("<h3 style='color:#264CAC;'>Principais Acontecimentos</h3>", unsafe_allow_html=True)

    st.markdown("<h3 style='color:#6C778A;'>Crise econômica de 2008:</h3>", unsafe_allow_html=True)
    st.write('''A crise econômica de 2008 é também conhecida como a crise financeira global...''')
    st.image('Imagens/Phyton/Python - Crise econômica de 2008.png', caption='Crise econômica de 2008')

    st.markdown("<h3 style='color:#6C778A;'>Impacto do acordo da OPEP:</h3>", unsafe_allow_html=True)
    st.write('A OPEP (Organização dos Países Exportadores de Petróleo)...')
    st.image('Imagens/Phyton/Python - Impacto acordo da OPEP.png', caption='Imapacto acordo da OPEP - 2016')

    st.markdown("<h3 style='color:#6C778A;'>Tensões geopolíticas do Oriente Médio:</h3>", unsafe_allow_html=True)
    st.write('As tensões geopolíticas no Oriente Médio em 2020 foram alimentadas principalmente pela rivalidade entre EUA e Irã...')
    st.image('Imagens/Phyton/Python - Tensão geopolíticas do oriente méido.png', caption='Tensão geopolítica do oriente médio - 2020')

    st.markdown("<h3 style='color:#6C778A;'>Pandemia covid-19</h3>", unsafe_allow_html=True)
    st.write('A pandemia de COVID-19, que começou no final de 2019 e se espalhou globalmente...')
    st.image('Imagens/Phyton/Python - Impacto da pandemia.png', caption='Pandemia Covid19 2020 - 2021')

elif pagina == "Dashboard Interativo":
    st.markdown("<h3 style='color:#264CAC;'>Dashboard Interativo</h3>", unsafe_allow_html=True)
    st.write("Aqui está o seu dashboard interativo.")

elif pagina == "MVP":
    st.markdown("<h3 style='color:#264CAC;'>MVP</h3>", unsafe_allow_html=True)
    # Código do MVP

elif pagina == "Conclusão":
    st.markdown("<h3 style='color:#264CAC;'>Conclusão</h3>", unsafe_allow_html=True)
    st.write("Aqui você pode escrever as conclusões do seu trabalho de pesquisa e as lições aprendidas.")

elif pagina == "Referências":
    st.markdown("<h3 style='color:#264CAC;'>Referências</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#6C778A;'>Crise financeira 2008</h3>", unsafe_allow_html=True)
    st.write('''https://www.investopedia.com/ask/answers/052715/how-did-financial-crisis-affect-oil-and-gas-sector.asp
    https://cepr.org/voxeu/columns/oil-prices-and-economic-recession-2007-08
    https://www.investopedia.com/articles/economics/09/financial-crisis-review.asp''')
    
    st.markdown("<h3 style='color:#6C778A;'>Informações OPEP</h3>", unsafe_allow_html=True)
    st.write('''https://www.ecb.europa.eu/pub/pdf/other/eb201608_focus01.en.pdf
    https://www.opec.org/opec_web/en/press_room/6748.htm
    https://oglobo.globo.com/economia/noticia/2023/11/30/o-que-e-a-opep-como-ela-funciona-e-o-que-o-brasil-tem-a-ganhar-caso-se-torne-um-membro.ghtml''')
    
    st.markdown("<h3 style='color:#6C778A;'>Tensões geopolíticas do oriente médio</h3>", unsafe_allow_html=True)
    st.write('''https://www.wilsoncenter.org/article/explainer-roots-and-realities-10-conflicts-middle-east
    https://www.iemed.org/publication/geopolitical-trends-shifts-challenges-and-fractures-of-the-post-arab-spring-2020-2021/
    https://www.brookings.edu/articles/the-middle-east-and-north-africa-over-the-next-decade-key-challenges-and-policy-options/''')
