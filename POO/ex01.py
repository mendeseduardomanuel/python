class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tendo {self.idade} anos.") 
pessoa1 = pessoa("Ariel", 22)
pessoa2 = pessoa("Flora", 20)
    
pessoa1.apresentar()
pessoa2.apresentar()