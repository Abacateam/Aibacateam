import streamlit as st
import requests
import pandas as pd

# URL da API
api_url = 'https://intranet.portodesantos.com.br/_json/porto_hoje.asp?tipo=programados2'

# Função para consumir a API
@st.cache_data
def get_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Falha ao obter os dados da API.')
        return None

#Pegando os Dataframes


data = get_data_from_api(api_url)
APS_Files = pd.DataFrame(data)
JUP_Files = pd.read_csv('Dte.csv', sep=';')
df2 = []

# Botão para carregar os dados

st.title('Dados do Porto de Santos - Programação de Navios')

button = st.button('Atualizar Informações')

for index, row in JUP_Files.iterrows():
    df2.append(row['Viagem'].replace(' ', '/'))

df2 = pd.DataFrame({
    'viagem': df2
})

st.dataframe(APS_Files)
st.dataframe(JUP_Files)

if button:
    st.cache_data.clear()
    data = get_data_from_api(api_url)

filtered_df = APS_Files[~APS_Files['viagem'].isin(df2['viagem'])]

st.dataframe(filtered_df)