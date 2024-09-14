import streamlit as st
import requests
import pandas as pd

# URL da API
api_url = "https://intranet.portodesantos.com.br/_json/porto_hoje.asp?tipo=programados2"

# Função para consumir a API
def get_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Falha ao obter os dados da API.")
        return None

# Função principal do Streamlit
def main():
    st.title("Dados do Porto de Santos - Programação de Navios")
    
    # Botão para carregar os dados
    if st.button("Carregar Dados"):
        data = get_data_from_api(api_url)
        
        if data:
            # Transformando os dados em um DataFrame para visualização
            df = pd.DataFrame(data)
            st.dataframe(df)
        else:
            st.error("Nenhum dado encontrado.")

if __name__ == "__main__":
    main()
