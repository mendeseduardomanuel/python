class MinhaClasse:
    def __init__(self) -> None:
        self.meu_atributo = 'Ola mundo'
    def me_metodo(self):
        print("Estou no metodo")
    
    def meu_metodo2(self,n,mult):
        return n * mult
objecto = MinhaClasse()
print(objecto.meu_atributo)
objecto.me_metodo()
result = objecto.meu_metodo2(3,2)
print(result)
