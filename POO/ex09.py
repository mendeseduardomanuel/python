class Calculadora:
    def __init__(self,n1,n2,res) -> None:
        self.n1 = n1
        self.n2 = n2
        self.res = res
    def Resultado(self):
        return"O resultado da operação é:"
class Soma(Calculadora):
    def __init__(self, n1, n2, res) -> None:
        super().__init__(n1, n2, res)
    def Resultado(self,n1,n2,res):
        return res == n1 + n2
class Subtracao(Calculadora):
    def __init__(self, n1, n2, res) -> None:
        super().__init__(n1, n2, res)
    def Resultado(self,n1,n2,res):
        return res == n1 - n2
class Multiplicacao(Calculadora):
    def __init__(self, n1, n2, res) -> None:
        super().__init__(n1, n2, res)
    def Resultado(self,n1,n2):
        return n1 * n2
class Divisao(Calculadora):
    def __init__(self, n1, n2, res) -> None:
        super().__init__(n1, n2, res)
    def Resultado(self,n1,n2):
        if n1 > n2:
            return n1 / n2
        else:
            return "Não é possivel dividir"

resultados = [Soma(2,2),Subtracao(2,2),Multiplicacao(2,2),Divisao(2,3)]

for Calculadora in resultados:
    print(Calculadora.Resultado()) 
    
    