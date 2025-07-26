"""
Adiciona o conteúdo do json (alfabeto.json) à variável constante ALFABETO (dict)
"""
import json
import os


_df = os.sep.join(__file__.split(os.sep)[0:-1]) + os.sep
_arquivo = 'alfabeto.json'
_caminho_arquivo = _df + _arquivo

with open(_caminho_arquivo, 'r', encoding='utf-8') as f:
    ALFABETO: dict = json.load(f)
