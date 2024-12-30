def ParImpar(n):
   while True:
    if n <= 0:
        break
    elif n % 2 == 0:
        return "O numero é par"
    else:
       return "O numero é impar"
    
n = int(input("Insira um numero: "))

print(ParImpar(n))