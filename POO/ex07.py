class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    def descriccao(self):
        return f"Veiculo: {self.nome}{self.modelo}"
class Carro(Veiculo):
    def __init__(self, marca, modelo,portas):
        super().__init__(marca, modelo)
        self.portas = portas
    def descriccao(self):
        return f"Carro: {self.marca} {self.modelo} {self.portas} portas"
class Moto(Veiculo):
    def __init__(self, marca, modelo,cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas
    def descriccao(self):
        return f"MOto: {self.marca} {self.modelo} {self.cilindradas} cc"
carro = Carro("Toyota","Corola",4)
moto = Moto("Honda","CB500",500)

print(carro.descriccao())
print(moto.descriccao())
