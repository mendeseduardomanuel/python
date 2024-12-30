
maior= 0
menor =float('inf')
for i in range(1,5):
    n = int(input("Insira um numero"))
    if n > maior:
        maior=n
    if n < menor:
        menor=n
print("O maior numero é: ",maior,end="")
print()
print("O menor numero é: ",menor,end="")
