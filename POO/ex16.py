class Pessoa:
    def __init__(self,nome,idade,cpf) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        
    def correr(self):
        print("Estou correndo")
        
    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
            print("Bebendo...")
          
    def __apresentar_documento(self):
        print(self.__cpf)
ronaldo = Pessoa('Ronaldo', 20, '02105725UE053')
ronaldo.beber('cerveja')
