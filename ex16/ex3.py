def Contar_Vogais_Consoantes(palavra):
    vogais = "aeiouAEIOU"
    NVogais = 0
    NConsoantes = 0
    for letra in palavra:
       if palavra.isalpha():
         if letra in vogais:
           NVogais += 1
         else:
           NConsoantes += 1
    return NVogais, NConsoantes
palavra = input("Insira uma palavra: ")
vogais, consoantes = Contar_Vogais_Consoantes(palavra)
print(f"Vogais: {vogais}, Consoantes: {consoantes}")