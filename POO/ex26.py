class DatabseConn:
    def __init__(self) -> None:
        self.__database = 'Postgres'
        self._conn = '//connection_string'
        self.user = 'Milaide'
        
    def get_database(self) -> None:
        print(self.__database)
        
    def _testing_connection(self) -> None:
        print('Connection OK')
class RepositorY(DatabseConn):
    def __init__(self) -> None:
        super().__init__()
        #print(self.user)
        #print(self.__database) error
        #print(self._conn)
    
    def select(self) -> None:
        self._testing_connection()
        print('connecting to {}'. format(self._conn))
        print('SELECT * FROM tablet')
        print(self.user)
        
repo = RepositorY()
repo.select()