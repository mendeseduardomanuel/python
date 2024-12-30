class Funcionario:
    
    def __init__(self,nome,salario) -> None:
        self.nome = nome
        self._salario = salario
    def apresntar(self):
        print(f"Funcionario {self.nome} e o seu salrio é de {self._salario} Kz")
class Gerente(Funcionario):
    def __init__(self, nome, salario,departamento) -> None:
        super().__init__(nome, salario)
        self.departamento = departamento
    def apresntar(self):
        print(f"Gerente {self.nome} o seu departamento é {self.departamento} tem o salrio de {self._salario} Kz")
 
funcionario = Funcionario("Flora",200000)
funcionario.apresntar()

gerente = Gerente("Delfina","Alimentação",300000)
gerente.apresntar()       