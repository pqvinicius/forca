#Projeto da Data Science Academy

import random
from os import system, name

def limpar():
    if name == "nt":
        _ = system('cls')
    else: _ = system('clear')
    
def jogo():
    limpar()
    print("\nBem-Vindo(a) ao nosso jogo da forca!\n")
    print("Adivinhe a palavra abaixo: ")
    
    with open('palavras_forca.txt', 'r', encoding='utf-8') as arquivo:
        palavras = [linha.strip() for linha in arquivo]
    palavra = random.choice(palavras)
    