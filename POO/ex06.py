'''
Polimorfismo permite que metodos com o mesmo 
nome em classes diferentes tenham comportamentos distintos
'''
class aniaml: 
    def __init__(self,nome):
        self.nome = nome
    def falar(self):
        print("Os animais emitem um som")
class Cachorro(aniaml):
    def falar(self):
        print(f"{self.nome} Diz : Au au!")
class Gato(aniaml):
    def falar(self):
        print(f"{self.nome} Diz: Miau miau!")

#Usando polimorfismo
animais = [Cachorro("Flora"), Gato("Gato")]

for animal in animais:
    print(animal.falar())