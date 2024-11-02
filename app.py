import streamlit as st

st.title('Tech Challenge 4 | Fiapp')
st.subheader('Introdução')

st.write('''Este trabalho tem como foco apresentar a análise do preço do petróleo brent, trazendo quatro acontecimentos que auxiliem a explicação das variação do preço e podem variar desde fatores geopolíticos até avanços tecnológicos. 
Traremos além dos acontecimentos, uma análise por meio de um dashboard dinâmico dos dados, previsão analisada e MVP.''')

st.title('Ferramentas utilizadas')
st.write(''''Para a realização deste trabalho, foi utilizado as seguintes ferramentas:
Python: utilizado para toda a tratativa inicial das bases como organização das colunas, remoção de espaços e duplicidades e valores nulo, assim como para a realização da previsão dos preços do petróleo por meio do modelo de machine learning PROPHET.
PowerBI: utilizado para a criação de um dashboard interativo compilando as informações disponíveis do preço do petróleo, previsão e acontecimentos que influenciam na explicação da variação do preço.
Streamlit: utilizado para desenvolvimento do MVP (Minimum Viable Product, ou Produto Mínimo Viável) e disponibilização das etapas e informações do projeto. ''''')

st.title('Metodologia')
st.subheader('Origem e análise dos dados')
st.write('Os dados utilizados nesta análise foram extraídos do site do Instituto de Pesquisa Econômica Aplicada (Ipea). Após a extração, os dados foram salvos em um arquivo csv, e importados no python para tratamentos iniciais mostrados abaixo:')
st. image ('Imagens/Phyton/Pyhton - importanto bibliotecas.png', caption='importando e instalando bibliotecasnecessárias')
st.image('Imagens/Phyton/Pyhton - tratamento dos dados.png', caption='importação da base de dados e tratamento inicial')
st.write('Após os tratamentos foi possível realizar a visualização gráfica dos seguintes acontecimentos:')

st.subheader('Crise econômica de 2008:')
st.write('Explicar o que foi a crise econômica')
st.image('Imagens/Phyton/Python - Crise econômica de 2008.png', caption='Crise econômica de 2008')

st.subheader('Impacto acordo da OPEP:')
st.write('Explicar o que foi o acordo da OPEP')
st.image('Imagens/Phyton/Python - Impacto acordo da OPEP.png', caption='Imapacto acordo da OPEP - 2016')

st.subheader('Tensões geopolíticas do oriente médio:')
st.write('Explicar o que é a tensão geopolítica no oriente médio')
st.image('Imagens/Phyton/Python - Tensão geopolíticas do oriente méido.png', caption='Tensão geopolítica do oriente médio - 2020')

st.subheader('Pandemia covid-19:')
st.write('Explicar o que foi a pandemia')
st.image('Imagens/Phyton/Python - Impacto da pandemia.png', caption='Pandemia Covid19 2020 - 2021')


st.subheader('Análise e visualizações de Dados e Insights')
st.subheader('Modelo de Machine Learning')
st.subheader('Conclusão')
