class Repositorio:
    def select(self, db_connection: any) -> None:
        conection = db_connection.conetar()
        print('Conectei ao banco {}. format(conection)')
        print('fazendo um SELECT * FROM...')
        db_connection.desconetar()
    
    def insert(self, db_connection: any) -> None:
        conection = db_connection.conetar()
        print('Conectei ao banco {}. format(conection)')
        print('fazendo um Insert Values...')
        db_connection.desconetar()