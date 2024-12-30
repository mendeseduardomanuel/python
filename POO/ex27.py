class Pessoa:
     def se_apresentar(self) -> None:
         print("Olá Sou pessoa A")

def apresentar():
    print('Estou alterando esse metodo')

class PessoaA(Pessoa):
    def __init__(self) -> None:
        super().__init__()
        
    def se_apresentar(self) -> None:
        print('Estou alterando esse metodo')
class PessoaB(PessoaA):
    def __init__(self) -> None:
        super().__init__()
        
pessoa = Pessoa()
pessoa.se_apresentar()

pessoaA = PessoaA()
pessoaA.se_apresentar()

pessoaB = PessoaB()
pessoaB.se_apresentar()   
    
