class PostgresDB:
    def __init__(self) -> None:
        self.__conexao = 'Postgres'
    def conectar(self) -> str:
        print('conectando ao banco Postgres...')
    def desconectando(self) ->str:
         print('Desconectando ao banco de dados...')   