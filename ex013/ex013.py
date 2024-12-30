while True:
    n1 = int(input("Insira o primeiro numero"))
    op = input("Insira o Operador(+,-,*,/)")
    n2 = int(input("Insira o segundo numero"))

    if n1 < 0 :
        print("Primeiro numero menor que zero")
    elif op != '+':
        print("Erro operador")
    else:
        match op:
            case'+':
                print(n1,"+",n2,"=",n1+n2)
                break
            case'-':
                print(n1,"-",n2,"=",n1-n2)
                break
            case'*':
                print(n1,"*",n2,"=",n1*n2)
                break
            case'/':
                if n1 > n2:
                    print(n1,"/",n2,"=",n1/n2)
                    break
                    