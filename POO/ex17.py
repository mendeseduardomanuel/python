#CALCULADORA
class Calculadora:
    def calcular(self, op,n1,n2):
        if op == '+':
           return self.__adicionar(n1,n2)
        elif op =='-':
           return  self.__subtrair(n1,n2)
        else:
            print("Operação invalida")
    def __adicionar(self,n1,n2):
        return n1 + n2
    def __subtrair(self,n1,n2):
        return n1 - n2
    
calculadora = Calculadora()
resultado = calculadora.calcular('+',2,2)
print(resultado)


