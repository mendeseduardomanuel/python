n = int(input("Insira um numero para calcular o seu fatorial"))
fatorial = 1
print(fatorial)
i = 1
for i in range(n):
    fatorial = fatorial * i
print("O fatorial de ", n, "é ", fatorial)