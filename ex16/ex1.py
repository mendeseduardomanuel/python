def Calculadora(n1, op, n2):
    match op:
        case'+':
            return n1 + n2
        case '-':
            return n1 - n2
        case '*':
            return n1 * n2
        case '/':
            return n1 / n2
        case _:
            return "Operador invalido"
        
n1 = float(input("Insira o primeiro numero: "))
op = input("Ecolha o operador(+,-,*,/)")
n2 = float(input("Insira o segundo numero: "))

print(n1, op ,n2, "=",Calculadora(n1,op,n2))