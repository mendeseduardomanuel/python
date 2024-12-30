class pessoa:
    #Atributo da class
    especie = "Homo sapiens"
    
    def __init__(self,nome,idade):
        #Atributos da instacia
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"O menu nome é {self.nome}, tenho {self.idade} e sou {pessoa.especie}")

pessoa1 = pessoa("Flora",20)
pessoa.especie = "Humano"
pessoa1.apresentar()        