class Casa:
    def __init__(self) -> None:
        self.__endereco = 'Rua dos limueros'
        self.__proprietario = None
    
    def acender_luzes(self) -> None:
        print('Estou Acendendo as luzes')
    def get_endereco(self) -> str:
        return self.__endereco
    
    def set_proprietario(self, proprietario: any) -> None:
        self.__proprietario = proprietario 
    def get_propriedade(self) -> any:
        return self.__proprietario       