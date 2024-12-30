class animal:
    #Função ou metodo(Instancia) Contrutor
    def __init__(self,nome,dono):
        #Atributo da instancia
        self.nome = nome
        self.dono = dono
    def apresentar(self):
        print(f"O nome do animal é {self.nome} e o seu nome é {self.dono}")
#Objectos
animal1 = animal("pit","Amarl")
animal2 = animal("flora","Mendes")

#Apresenrtação dos objectos
animal1.apresentar()
animal2.apresentar()
