class Mae:
    def __init__(self,endereco) -> None:
        self.endereco = endereco
        self.sobrenome = 'Silava'
    def comer(self) -> None:
        print('Estou comendo....')
    def estudar(self) -> None:
        print('Estou estudando...')

class Filha(Mae):
    def __init__(self) -> None:
        super().__init__('Rua do Bolo')
    def brincar(self, brinquedo: str) -> None:
        print('Estou brincando com {}'. format(brinquedo))
clara = Filha()
clara.estudar()
clara.brincar('boneca')
print(clara.endereco)
