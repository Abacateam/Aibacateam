# 🎈 Dashboard AIbacate

O Protótipo do time Abacateam para o evento Porto Hack Santos 2024

### Como rodar a aplicação

1. Instalar as dependências

   ```
   $ pip install -r requirements.txt
   ```

2. Rodar o app

   ```
   $ streamlit run Chegada.py
   ```

3. Simulando falha no envio do status da carga:

   # No arquivo Dte.csv:
   Remova o seguinte index:
   
   **9706190;;CAPE AKRITAS;3919 2024;;BRASIL TERM. PORTUARIO - OPERADOR PORTUA;08/09/2024 00:00;;13/09/2024 19:00;;;Nao**

   Após isso, salve e recarregue a página
