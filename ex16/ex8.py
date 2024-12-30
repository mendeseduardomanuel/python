def Verifica_Primo(n):
    if n <= 1 :
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Insira Um numero: "))
if Verifica_Primo(n):
    print(f"{n} é um numero primeo")
else:
    print(f"{n} não é um numero primo")