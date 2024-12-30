'''
Encapsulamento é controlar o acesso aos atributos:

Publicos,protegido(_) e privados(__),
'''
class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self._saldo = saldo
        self.__senha = "123"
    def Deposito(self, valor):
        self._saldo += valor
        print(f"Deposito Realizado! saldo atual {self._saldo}")
    def __mostrar_senha(self):
        return self.__senha
    
conta = ContaBancaria("Flora", 1000)

print(conta.titular)
print(conta._saldo) 
