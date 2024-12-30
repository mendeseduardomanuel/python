'''
Herança é erdar atributos e metodos de outra class.
'''
class animal:
    def __init__(self,nome):
        self.nome = nome
    def falar(self):
        print("O animal emite um som.")
class Cachorro(animal):
    def falar(self):
        print(f"{self.nome} diz : AU au!")
class Gato(animal):
    def falar(self):
        print(f"{self.nome} Diz : Miau!")
        
cachorro = Cachorro("pit")
gato = Gato("Flora")

cachorro.falar()
gato.falar() 