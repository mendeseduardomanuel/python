class MinhaClasse:
    estatico = 'Mendes'
    
    def __init__(self, estado: str) -> None:
        self.estado = estado
        
obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

print(obj1.estatico)
print(obj2.estatico)