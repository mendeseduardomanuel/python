lista = []

for _ in range(3):
    pessoas = {}

    pessoas["nome"] = input("Insira o seu nome")
    pessoas["altura"] = float(input("Insira a sua altura"))
    pessoas["idade"] = int(input("Insira a sua idade"))
    lista.append(pessoas)

print("Dados das pesoas: ")
print()
for pessoas in lista:
    print("Nome: ", pessoas["nome"])
    print("Altura: ", pessoas["altura"])
    print("Idade: ", pessoas["idade"])