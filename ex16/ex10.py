import random

def jogo_da_forca():
    palavras = ["python", "programacao", "jogo", "desafio", "computador"]
    palavra_secreta = random.choice(palavras).upper()
    letras_acertadas = ["_"] * len(palavra_secreta)
    tentativas = 6
    letras_erradas = []

    print("Bem-Vindo ai Jogo da Forca!")
    print("Palavras Secretas:", " ".join(letras_acertadas))

    while tentativas > 0 and  "_" in letras_acertadas:

        print("\nChances Restantes:", tentativas)
        print("letras erradas:"," ".join(letras_erradas))

        letra = input("Insira uma letra: ").upper()

        if len(letra) != 1 or not letra.isalpha() :
            print("Entrada Invalida! Digite apenas uma letra.")
            continue
        if letra in letras_acertadas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra_secreta:
            print(f"Boa! A letra '{letra}' está na palavra.")
            for i, char in enumerate(palavra_secreta):
                if char == letra:
                    letras_acertadas[i] = letra
        else:
            print(f"A letra '{letra}' não está na palavra.")
            letras_erradas.append(letra)
            tentativas -= 1
        
        print("Palavra Secreta:", " ".join(letras_acertadas))

    if " _ " not in  letras_acertadas:
        print("\n Parabéns! Você acertou a palavra:", palavra_secreta)
    else:
        print("\nVocê perdeu! A palavra era:", palavra_secreta)

jogo_da_forca()

