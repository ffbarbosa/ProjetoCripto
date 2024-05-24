import requests # importação da biblioteca request 
from bs4 import BeautifulSoup as bs # importção do bs4 
import streamlit as st

class PrecoBitcoin:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def busca_dados(self):
        resposta = requests.get(self.url)
        if resposta.status_code == 200:
            self.soup = bs(resposta.content, "html.parser")
        else:
            raise Exception(f"Falha ao buscar dados. Código de status: {resposta.status_code}")

    def obter_preco(self):
        if self.soup:
            preco = self.soup.find("div", {"class": "css-1bwgsh3"})
            return preco.text if preco else "Preço não encontrado"
        else:
            raise Exception("Soup não está inicializado. Chame busca_dados() primeiro.")

test




