import streamlit as st
import pandas as pd
import numpy as np
from model_lstm import load_lstm_model, predict_with_lstm
from scaler_util import scale_data, inverse_scale_data

st.markdown("<p style='font-size:40px; color:#B40C40;'>Tech Challenge 4 | Fiap</p>", unsafe_allow_html=True)

st.markdown("<h3 style='color:#264CAC;'>Introdução</h3>", unsafe_allow_html=True)

st.write('''Este trabalho tem como foco apresentar a análise do preço do petróleo brent, trazendo quatro acontecimentos que auxiliem a explicação das variação do preço e podem variar desde fatores geopolíticos até avanços tecnológicos. 
Traremos além dos acontecimentos, uma análise por meio de um dashboard dinâmico dos dados, previsão analisada e MVP.''')

st.markdown("<h3 style='color:#264CAC;'>Ferramentas utilizadas</h3>", unsafe_allow_html=True)
st.write(''''Para a realização deste trabalho, foi utilizado as seguintes ferramentas:
Python: utilizado para toda a tratativa inicial das bases como organização das colunas, remoção de espaços e duplicidades e valores nulo, assim como para a realização da previsão dos preços do petróleo por meio do modelo de machine learning PROPHET.
PowerBI: utilizado para a criação de um dashboard interativo compilando as informações disponíveis do preço do petróleo, previsão e acontecimentos que influenciam na explicação da variação do preço.
Streamlit: utilizado para desenvolvimento do MVP (Minimum Viable Product, ou Produto Mínimo Viável) e disponibilização das etapas e informações do projeto. ''''')

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

st.markdown("<h3 style='color:#264CAC;'>Acontecimentos que influenciaram o preço do petróleo</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#6C778A;'>Crise econômica de 2008:</h3>", unsafe_allow_html=True)
st.write('''A crise econômica de é também conhecida como a crise financeira global, foi uma das mais graves desde a Grande Depressão de 1929. Ela teve início nos Estados Unidos e rapidamente se espalhou para o resto do mundo, afetando bancos, mercados financeiros, empresas e, principalmente, a vida de milhões de pessoas.
Nos anos que antecederam a crise, os preços dos imóveis nos Estados Unidos subiram muito. Essa "bolha imobiliária" foi alimentada por políticas de crédito fácil: os bancos ofereciam empréstimos com juros baixos e condições flexíveis, mesmo para pessoas com pouca capacidade de pagamento (os chamados "subprime"), com todas essas condições muitas pessoas compraram imóveis, levando a uma alta na demanda e, consequentemente, alta no preço das casas.
Os bancos e instituições financeiras começaram a "empacotar" esses empréstimos de alto risco em títulos e vendê-los no mercado financeiro como investimentos seguros que prometiam retornos elevados e pareciam ser uma maneira segura de investir em imóveis, que tradicionalmente eram vistos como ativos seguros.
Em 2006, os preços dos imóveis começaram a cair, e os proprietários que haviam comprado casas com empréstimos subprime ficaram com dívidas maiores do que o valor das próprias casas, ao não conseguirem arcar com as parcelas foram obrigados a entregar seus imóveis aos bancos, que passaram a ter grandes quantidades de casas em seu inventário, o que aumentou ainda mais a oferta de imóveis e fez com que os preços caíssem ainda mais.
Como os títulos lastreados em hipotecas haviam sido amplamente vendidos e estavam espalhados por todo o sistema financeiro global, a queda no valor dos imóveis causou grandes prejuízos, bancos e seguradoras que tinham esses títulos em suas carteiras (como o Lehman Brothers e a AIG) sofreram perdas massivas.
Isso resultou em uma crise de confiança: os bancos pararam de emprestar entre si, temendo que o outro não conseguisse pagar a dívida. Esse congelamento de crédito afetou empresas e consumidores, que passaram a ter mais dificuldade de obter financiamento.
Em setembro de 2008, o banco Lehman Brothers declarou falência, o que marcou um ponto crítico da crise. A falência de uma instituição financeira desse porte trouxe ainda mais incerteza para o mercado.
Para evitar uma catástrofe financeira, o governo dos EUA e de outros países intervieram, injetando bilhões de dólares em pacotes de resgate para estabilizar o sistema financeiro. 
A crise financeira rapidamente se espalhou para a economia real, levando à recessão em vários países. Empresas cortaram custos, demitiram funcionários, e o desemprego disparou, a confiança do consumidor e dos investidores despencou, o que resultou em queda no consumo e investimentos. A recuperação foi lenta, e muitos países continuaram a sentir os efeitos da crise por vários anos.


A crise teve um impacto significativo no preço dos combustíveis, causado principalmente pela desaceleração econômica global que reduziu a demanda por petróleo, logo no início da crise o preço do petróleo subiu devido a preocupações geopolíticas e à especulação financeira, atingindo níveis recordes. No entanto, quando a crise se aprofundou, o consumo global de petróleo caiu drasticamente, levando a uma redução acentuada nos preços — de cerca de $147 por barril em julho de 2008 para aproximadamente $32 no final do ano. 
Esse colapso foi impulsionado tanto pela queda da demanda quanto pela diminuição da atividade econômica, que reduziu a necessidade de combustíveis em vários setores industriais e de transporte.
As dificuldades financeiras das empresas de energia, que enfrentaram problemas de crédito e financiamento, também contribuíram para a instabilidade dos preços. Além disso, a volatilidade no setor de commodities levou a um ajuste no investimento em novas explorações e produção, o que impactou a oferta no médio prazo. Para mais detalhes sobre esse período e suas consequências, você pode conferir artigos do Center for Economic Policy Research e do Brookings Institute, que analisam o efeito da crise no mercado de petróleo e suas implicações econômicas''')
st.image('Imagens/Phyton/Python - Crise econômica de 2008.png', caption='Crise econômica de 2008')

st.markdown("<h3 style='color:#6C778A;'>Impacto do acordo da OPEP:</h3>", unsafe_allow_html=True)
st.write('''A OPEP (Organização dos Países Exportadores de Petróleo e Aliados) que foi criada em 1960 inicialmente por 5 países que exportam petróleos e ao longo dos anos outros paises foram convidados a participar.
Ela foi criada com o objetivo de estabelecer uma política comum em relação à produção e à venda de petróleo, de forma a influenciar os preços do petróleo no mercado internacional. Por serem grandes produtores, seus membros são capazes mexer com as cotações, ao aumentar ou cortar a produção de forma coordenada.
Em 2016, quando os preços do petróleo estavam particularmente baixos, a Opep uniu forças com outros dez grandes produtores de petróleo para criar a Opep+, que tinha como missão reduzir a produção de petróleo e estabilizar o mercado global de energia. A decisão inicial ocorreu em setembro de 2016, durante a reunião em Argel, onde membros da OPEP concordaram em limitar a produção pela primeira vez desde 2008. Em novembro, a OPEP finalizou o acordo, e em dezembro, países não-membros (incluindo Rússia, México e outros) se comprometeram voluntariamente a cortes de produção, formando uma coalizão inédita para controlar o excesso de oferta global de petróleo.
Essas restrições resultaram em aumentos moderados nos preços do petróleo e ajudaram a recuperar parte da estabilidade do mercado.O acordo se mostrou crucial para amortecer impactos de oscilações no preço do petróleo nos anos seguintes, especialmente durante crises.''')
st.image('Imagens/Phyton/Python - Impacto acordo da OPEP.png', caption='Imapacto acordo da OPEP - 2016')

st.markdown("<h3 style='color:#6C778A;'>Tensões geopolíticas do oriente médio::</h3>", unsafe_allow_html=True)
st.write('''As tensões geopolíticas no Oriente Médio em 2020 foram alimentadas principalmente pela rivalidade entre Estados Unidos e Irã e pelo conflito prolongado no Iêmen, que envolveu diversas potências regionais. As hostilidades entre EUA e Irã escalaram após o assassinato do general iraniano Qassem Soleimani em janeiro de 2020 por um ataque de drone dos EUA em Bagdá. Esse ato provocou uma resposta militar do Irã, que atacou bases americanas no Iraque. Em meio a essas tensões, os ataques iranianos a instalações petrolíferas sauditas em 2019 também mostraram o quanto a segurança energética global estava em risco, elevando a volatilidade no mercado de petróleo.
O cenário já estava complicado pelo apoio do Irã a grupos na Síria, Iraque e Líbano, bem como ao grupo Houthi no Iêmen, que estava em conflito com uma coalizão liderada pela Arábia Saudita. Esse apoio provocou intensificação nas rivalidades, com impactos devastadores, como a piora da crise humanitária no Iêmen e a instabilidade nas fronteiras regionais. A pandemia de COVID-19 complicou ainda mais as relações e dificultou o progresso diplomático, embora houvesse algumas tentativas de mediação e reaproximação entre países do Golfo, como os Emirados Árabes Unidos e o Irã, principalmente devido ao impacto econômico da pandemia nas economias dependentes de petróleo da região.
Essas tensões contribuíram para um cenário de incerteza, aumento de riscos e volatilidade nos preços de energia em 2020, destacando a importância de estabilidade na região para o mercado global de petróleo e para a segurança econômica.''')
st.image('Imagens/Phyton/Python - Tensão geopolíticas do oriente méido.png', caption='Tensão geopolítica do oriente médio - 2020')

st.markdown("<h3 style='color:#6C778A;'>Pandemia covid-19</h3>", unsafe_allow_html=True)
st.write('''A pandemia de COVID-19, que começou no final de 2019 e se espalhou globalmente em 2020, resultou em uma crise de saúde sem precedentes que afetou todos os aspectos da vida cotidiana, levando a bloqueios, restrições de viagem e mudanças significativas nos padrões de consumo e produção. As economias foram severamente impactadas, com muitos setores enfrentando quedas drásticas na demanda.
Com a implementação de lockdowns e restrições de movimentação em todo o mundo, a demanda por petróleo caiu drasticamente. Indústrias, transporte e aviação sofreram com reduções severas no consumo. A demanda global de petróleo caiu cerca de 20% em abril de 2020, o que levou a um excesso de oferta significativo.
Em abril de 2020, o preço do petróleo alcançou um marco histórico com o petróleo WTI (West Texas Intermediate) chegando a valores negativos pela primeira vez, refletindo que os produtores estavam dispostos a pagar para que as pessoas retirassem o petróleo de seus estoques, dado o colapso da demanda e a falta de capacidade de armazenamento.''')
st.image('Imagens/Phyton/Python - Impacto da pandemia.png', caption='Pandemia Covid19 2020 - 2021')


st.markdown("<h3 style='color:#264CAC;'>Criação de Dashboard interativo</h3>", unsafe_allow_html=True)

st.markdown("<h3 style='color:#264CAC;'>MVP</h3>", unsafe_allow_html=True)

# Configurações iniciais do Streamlit
st.title("Previsão de Preço do Petróleo Brent")
st.write("Aplicação de previsão de preços usando modelo LSTM.")

# Parâmetros e caminhos dos arquivos
model_path = 'model_lstm/model_lstm.h5'
scaler_path = 'model_lstm/scaler.joblib'
sequence_length = 10  # Definido na etapa de treinamento

# Carregar o modelo e scaler
st.sidebar.header("Configurações de Previsão")
num_prediction = st.sidebar.slider("Número de dias para prever", min_value=1, max_value=30, value=7)

try:
    model = load_lstm_model(model_path)
except FileNotFoundError:
    st.error("Erro: Modelo LSTM não encontrado. Verifique o caminho do arquivo.")

# Carregar e exibir os dados de entrada
uploaded_file = st.file_uploader("Envie um arquivo Excel com os dados de Brent", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Dados Carregados:")
    st.write(df.tail())

    # Normalizar os dados com o scaler
    try:
        data_scaled = scale_data(df[['Close']].values, scaler_path)
    except FileNotFoundError:
        st.error("Erro: Scaler não encontrado. Verifique o caminho do arquivo.")
    else:
        # Fazer previsões
        predictions = predict_with_lstm(model, data_scaled, num_prediction, sequence_length, scaler_path)
        
        # Preparar e exibir o dataframe de resultados
        future_dates = pd.date_range(df['Data'].iloc[-1] + pd.Timedelta(days=1), periods=num_prediction)
        forecast_df = pd.DataFrame({'Data': future_dates, 'Previsão': predictions.flatten()})
        
        st.write("Previsão para os próximos dias:")
        st.write(forecast_df)
        
        # Gráfico dos resultados
        st.line_chart(forecast_df.set_index('Data'))
else:
    st.info("Aguarde o upload do arquivo para gerar previsões.")

model_lstm.py

##Funções para carregar o modelo e fazer previsões.

import os
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from scaler_util import inverse_scale_data  # Para desnormalizar as previsões

# Função para carregar o modelo salvo
def load_lstm_model(model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError("O arquivo do modelo LSTM não foi encontrado.")
    model_lstm = load_model(model_path)
    return model_lstm

# Função para fazer previsões com o modelo LSTM
def predict_with_lstm(model, data_scaled, num_prediction, sequence_length, scaler_path):
    prediction_list = list(data_scaled[-sequence_length:])
    for _ in range(num_prediction):
        x = np.array(prediction_list[-sequence_length:]).reshape((1, sequence_length, 1))
        out = model.predict(x)[0][0]
        prediction_list.append([out])

    # Obtem somente as novas previsões geradas
    prediction_list = prediction_list[-num_prediction:]
    return inverse_scale_data(np.array(prediction_list).reshape(-1, 1), scaler_path)

# Função para avaliar o modelo LSTM
def evaluate_lstm_model(model, X_test, y_test, scaler_path):
    predictions = model.predict(X_test)
    predictions = inverse_scale_data(predictions, scaler_path)
    y_test = inverse_scale_data(y_test, scaler_path)
    
    r2 = r2_score(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    mape = np.mean(np.abs((y_test - predictions) / y_test)) * 100
    rmse = np.sqrt(mse)
    return r2, mse, mae, mape, rmse

scaler_util.py
Funções para carregar, escalar e desescalar os dados usando o scaler.

import os
import joblib
import numpy as np

# Função para carregar o scaler salvo
def load_scaler(scaler_path):
    if not os.path.exists(scaler_path):
        raise FileNotFoundError("O arquivo do scaler não foi encontrado.")
    scaler = joblib.load(scaler_path)
    return scaler

# Função para escalar os dados
def scale_data(data, scaler_path):
    scaler = load_scaler(scaler_path)
    return scaler.transform(data)

# Função para desescalar os dados
def inverse_scale_data(scaled_data, scaler_path):
    scaler = load_scaler(scaler_path)
    return scaler.inverse_transform(scaled_data)

train_lstm.py
Funções para carregar os dados, treinar o modelo LSTM, e salvar o modelo e o scaler.

import os
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler
import joblib
from model_lstm import evaluate_lstm_model
from scaler_util import scale_data

# Função para carregar e preprocessar os dados
def load_and_process_data(excel_path, data_corte):
    df = pd.read_excel(excel_path)
    df = df.rename(columns={'Brent': 'Close'})
    df['Data'] = pd.to_datetime(df['Data'])
    df = df[df['Data'] > data_corte]
    df.reset_index(drop=True, inplace=True)
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(df[['Close']])
    return df, data_scaled, scaler

# Função para criar sequências de dados
def create_sequences(data, sequence_length):
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i+sequence_length])
        y.append(data[i+sequence_length])
    return np.array(X), np.array(y)

# Função para construir e treinar o modelo LSTM
def train_lstm_model(X_train, y_train, sequence_length, epochs=100, batch_size=64):
    model = Sequential([
        LSTM(350, input_shape=(sequence_length, 1)),
        Dense(1)
    ])
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)
    return model

# Função para treinar o modelo LSTM e salvar o modelo e scaler
def train_and_save_model(excel_path, model_path, scaler_path, data_corte, sequence_length):
    df, data_scaled, scaler = load_and_process_data(excel_path, data_corte)
    train_size = int(len(data_scaled) * 0.8)
    X_train, y_train = create_sequences(data_scaled[:train_size], sequence_length)
    X_test, y_test = create_sequences(data_scaled[train_size:], sequence_length)
    
    model = train_lstm_model(X_train, y_train, sequence_length)
    r2, mse, mae, mape, rmse = evaluate_lstm_model(model, X_test, y_test, scaler_path)
    
    model.save(model_path)
    joblib.dump(scaler, scaler_path)
    
    print(f"R² Score: {r2}")
    print(f"MSE: {mse}")
    print(f"MAE: {mae}")
    print(f"MAPE: {mape}")
    print(f"RMSE: {rmse}")

# Script principal
if _name_ == "_main_":
    base_dir = os.path.dirname(os.path.abspath(_file_))
    excel_path = os.path.join(base_dir, 'dataset', 'Petroleo.xlsx')
    model_path = os.path.join(base_dir, 'model_lstm', 'model_lstm.h5')
    scaler_path = os.path.join(base_dir, 'model_lstm', 'scaler.joblib')
    
    data_corte = pd.to_datetime('2020-05-03')
    sequence_length = 10

    train_and_save_model(excel_path, model_path, scaler_path, data_corte, sequence_length)

st.markdown("<h3 style='color:#264CAC;'>Conclusão</h3>", unsafe_allow_html=True)



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
