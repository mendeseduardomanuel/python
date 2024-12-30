import random

matriz = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]

print("Matriz 3*3: ")
for linnha in matriz:
    print(linnha)

soma_linha = [sum(linha) for linha in matriz]
soma_colunas = [sum(matriz[i][j] for i in range(3)) for j in range(3)]
soma_diagonal_principal = sum(matriz[i][i] for i in range(3))
soma_diagonal_secundaria = sum(matriz[i][2 - i] for i in range(3))

print("\n Soma de Linha:", soma_linha)
print("Soma de colunas:", soma_colunas)
print("Soma diagonal principal:", soma_diagonal_principal)
print("Soma diagonal Secundaria:", soma_diagonal_secundaria)