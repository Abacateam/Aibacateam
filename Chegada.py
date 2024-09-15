import streamlit as st
import requests
import pandas as pd

# Custom CSS for styling the sidebar

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #FFB44A;
    width: 240px;
    
}
</style>""", unsafe_allow_html=True)

def card_style(card_title, card_color, *addtional_title):
    if addtional_title:
        st.markdown(
            f"""
        <div style='background-color: {card_color}; 
                    padding: 20px; 
                    border-radius: 10px;
                    margin: 10px 0;'>
            <p text-align: center;'>{card_title}</p>
            <p text-align: center;'>{addtional_title[0]}</p>
        </div>
        """, unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style='background-color: {card_color}; 
                        padding: 20px; 
                        border-radius: 10px;
                        margin: 10px 0;'>
                <p text-align: center;'>{card_title}</p>
            </div>
            """, unsafe_allow_html=True
        )

# URL da API
api_url = 'https://intranet.portodesantos.com.br/_json/porto_hoje.asp?tipo=programados2'

# Função para consumir a API

def get_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Falha ao obter os dados da API.')
        return None

# Pegando os Dataframes


data = get_data_from_api(api_url)
APS_Files = pd.DataFrame(data)
JUP_Files = pd.read_csv('Dte.csv', sep=';')
checkContainers = False

def get_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Falha ao obter os dados da API.')
        return None

# Pegando os Dataframes


data = get_data_from_api(api_url)
APS_Files = pd.DataFrame(data)
JUP_Files = pd.read_csv('Dte.csv', sep=';')

df = []
df2 = []

# Botão para carregar os dados

for index, row in JUP_Files.iterrows():
    df2.append(row['Viagem'].replace(' ', '/'))

df2 = pd.DataFrame({
    'viagem': df2
})
for index, row in APS_Files.iterrows():
    df.append(row['viagem'].replace('/', ' '))

df = pd.DataFrame({
    'Viagem': df
})

filtered_df = JUP_Files[~JUP_Files['Viagem'].isin(df['Viagem'])]
filtered_df2 = APS_Files[~APS_Files['viagem'].isin(df2['viagem'])]

rowRecintos = st.columns(4)
recintos = ['Santos Brasil', 'Ecoporto', 'BTP', '...']
index = 0

for col in rowRecintos:

    checkOkay = True
    if filtered_df2.iloc[0]["local"] == recintos[index]:
        checkOkay = False
        checkContainers = True
    if checkOkay == False:
        with col:
            card_style((recintos[index]),  '#FF766E')
            col.write('Atenção!')
            index += 1
            continue
    else:
        with col:
            card_style((recintos[index]),  '#71D88B')
            col.write('Operando')
            index += 1

if checkContainers == True:
    col1, col2 = st.columns([0.65, 0.35])

    with col1:
        card_style('Nome Navio: ' + filtered_df2.iloc[0]["nomenavio"], '#D9E9E8')
        card_style('IMO: ' + str(filtered_df2.iloc[0]["imo"]), '#7FCCB8')
        card_style('Manobra: ' + filtered_df2.iloc[0]['manobra'], '#51BEAB')
        card_style('Louyd: Faltando', '#309B91')
        card_style('Viagem: ' + filtered_df2.iloc[0]['viagem'], '#1A6A6B')
    with col2:

        card_style('Data de Chegada: ' + filtered_df2.iloc[0]['data'],
                '#36D3CC', 'Hora Chegada: ' + filtered_df2.iloc[0]['periodo'])
        button2 = st.button("Enviar Aviso")

        if button2:
            st.write('Em breve!')
