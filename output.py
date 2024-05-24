
from test import PrecoBitcoin
import streamlit as st 

# Exemplo de uso
url = "https://www.binance.com/pt/price/bitcoin"
raspador = PrecoBitcoin(url)
raspador.busca_dados()
preco = raspador.obter_preco()
st.write("BTC Dólar: " + preco)

