contador = 0

while True:
    print(f"contador{contador}")
    print("Escolha uma opção")
    print("1-Incrementar o contador")
    print("2-Encerrar o Programa")
    
    opcao = input("Digite a sua opção: ")
    
    if opcao=="1":
        contador +=1
        continue
    elif opcao == "2":
        print("Programa encerrado")
        break
    else:
        print("Opção invalida")
        