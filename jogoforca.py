#Projeto da Data Science Academy

import random
from os import system, name

def limpar():
    if name == "nt":
        _ = system('cls')
    else: _ = system('clear')