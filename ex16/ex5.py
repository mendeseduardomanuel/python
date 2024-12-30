def Fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Fatorial(n-1)
n = int(input("Insira um numero"))
print("O fatoria de ",n, "é: ",Fatorial(n))