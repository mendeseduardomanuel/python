class ControlRemoto:
    def __init__(self,televisao,comodo) -> None:
        self.televisao = televisao
        self.comodo = comodo
    def avancar_canal(self):
        print("Canal Avançado")
    def voltar_canal(self):
        print("Voltar o canal")
    def escolher_canal(self, canal):
        print("alterar para o canal:{}". format(canal))
        
control = ControlRemoto("Samsung", "sala")
print(control.comodo)
print(control.televisao)
control.avancar_canal()
control.escolher_canal(12)