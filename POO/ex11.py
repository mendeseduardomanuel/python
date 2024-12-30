class SistemaBancario:
    def __init__(self,titular,saldo) -> None:
        self.titular = titular
        self.__saldo = saldo
    def Deposito(self, valor):
        if valor > 0 :
            self.__saldo += valor
            print(f"Foi depositado {valor} na sua conta")
        else:
            print("Valor Invalido")
    def Levantamento(self,valor):
        if valor > 0 and valor <= self.__saldo: 
            self.__saldo -= valor
            print(f"Foi levantado {valor} com sucesso!")
        else:
            print("Levantamento Invalido")
    def Consulta(self):
        print(f"O saldo da sua conta é {self.__saldo}")
        
conta = SistemaBancario("Flora", 5000)
conta.Consulta()

conta.Deposito(5000)
conta.Consulta()

conta.Levantamento(200)
conta.Consulta()