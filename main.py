# -*- coding: utf-8 -*-
"""
Faz a tradução de letras para Erin
"""
from configs.alfabeto import ALFABETO


def tratamento(p: str) -> str:
    """ Remove letras repetidas da palavra """
    p = p.lower().strip()
    aux = ' '
    for letra in p:
        if letra != aux[-1]:
            aux += letra
    aux = aux.strip()
    return aux
    

def traduzir_alphaerin(p: str) -> str:
    """ Faz a tradução de letras para Erin """
    p = tratamento(p)
    aux = ''
    for letra in p:
        aux += ALFABETO['alphaErin'].get(letra, letra)
    aux = tratamento(aux)
    return aux


try:
    while True:
        palavra = input('Digite alguma koisa:\n>')
        if palavra:
            palavra_traduzida = traduzir_alphaerin(palavra)
            print(palavra_traduzida, '\n')

except KeyboardInterrupt:
    pass
