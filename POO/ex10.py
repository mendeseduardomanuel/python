class Retangulo:
    def __init__(self,largura,altura) -> None:
        self.largura = largura
        self.altura = altura
    def Calculo_area(self):
        return self.largura * self.altura
    def Calculo_perimetro(self):
        return 2 * (self.largura + self.altura)
    
largura = float(input("Insira a largura do retangulo: "))
altura = float(input("Insira a altura do retangulo: "))

retangulo = Retangulo(largura,altura)

print(f"A area do retangulo é: {retangulo.Calculo_area()}")
print(f"O perimetro do retangulo é: {retangulo.Calculo_perimetro()}")