import mysql.connector

'''
Para integrar o myql no nosso codigo python temos de integrar o mysql no python instalando-o da seguinte maneira:

pip install mysql-connector-python
'''

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='crud_python',
)

cursor = conexao.cursor()
#CRUD

#CREATE
#nome_produto = "TV"
#valor = 50000
#comando = f'INSERT INTO vendas(nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)
#conexao.commit() #Editando o Banco de dados

#READE

#comando = f'SELECT * FROM vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)

#UPDEATE

#nome_produto = "TV"
#valor = 20
#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() #Edita o banco de dados

#DELETE

#nome_produto = "TV"
#comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()


cursor.close()
conexao.close()