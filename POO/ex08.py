class Acessorio:
    def __init__(self,descricao,marca,valor) -> None:
        self.descricao = descricao
        self.marca = marca
        self._valor = valor
    def apresentacao(self):
        print("Os acessorios são:")
class Pasta(Acessorio):
    def __init__(self, descricao, marca, valor) -> None:
        super().__init__(descricao, marca, valor)
    def apresentacao(self):
        return f"{self.descricao} a sua marca é {self.marca} e cutas {self._valor} kz"

class Chapeu(Acessorio):
    def __init__(self, descricao, marca, valor) -> None:
        super().__init__(descricao, marca, valor)
    def apresentacao(self):
        return f"{self.descricao} a sua marca é {self.marca} e cutas {self._valor} kz"

Acessorios = [Pasta("Para Mulher","Gucci",22.000), Chapeu("Para Homem","New York",2000)]

for Acessorio in Acessorios:
    print(Acessorio.apresentacao())