def Soma(n1, n2):
    return n1 + n2
def Subtracao(n1, n2):
    return n1 - n2
def Multiplicacao(n1, n2):
    return n1 * n2
def Divisao(n1, n2):
    return n1 / n2 if n2 != 0 else "Divisão por Zero não é permitido"

n1 = int(input("Insira o primeiro numero: "))
n2 = int(input("Insira o segundo numero: "))
op= input("Insira o operador(+,-,/,*): ")

match op:
    case'+':
        print("Resultado:", Soma(n1,n2))
    case'-':
        print("Resultado:", Subtracao(n1,n2))
    case'*':
        print("Resultado:", Multiplicacao(n1,n2))
    case'/':
        print("Resultado:", Divisao(n1,n2))
    case _:
        print("Operador errado")