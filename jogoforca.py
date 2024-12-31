# Projeto da Data Science Academy

import random
from os import system, name

def limpar():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')
    
def jogo():
    limpar()
    print("\nBem-Vindo(a) ao nosso jogo da forca!\n")
    print("Adivinhe a palavra abaixo: ")
    
    with open('C:/Users/User/Documents/PROJETOS/PYTHON/Jogo da Forca/palavras_forca.txt', 'r', encoding='utf-8') as arquivo:
        palavras = [linha.strip() for linha in arquivo]
    
    # Escolher uma palavra aleatória
    palavra = random.choice(palavras).lower()
    letras_descobertas = ["_" for _ in palavra]
    chances = 5
    letras_erradas = []
      
    while chances > 0:
        print("\n" + " ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", ", ".join(letras_erradas))
        
        tentativa = input("\nDigite uma letra: ").lower()
        
        if tentativa in letras_descobertas or tentativa in letras_erradas: 
            print("Você já escolheu essa letra, por favor, escolha outra:")
            continue
        if tentativa in palavra:
            index = 0
            for l in palavra:
                if tentativa == l:
                    letras_descobertas[index] = l
                index +=1
        else: 
            print("Essa letra não faz parte da palavra :(")
            chances -= 1
            letras_erradas.append(tentativa)
            
        if "_" not in letras_descobertas:
            print("Parabéns, você venceu! A palavra era:", palavra)
            break
        
    if "_" in letras_descobertas:
        print("Que pena, você perdeu, a palavra era: ", palavra)
        denovo = input("Gostaria de tentar novamente: S/N:")
        if denovo == "S":
                jogo()
        else: 
            print("Obrigado por ter jogado o nosso jogo. Volte sempre!")
        
if __name__ == "__main__":
    jogo()
