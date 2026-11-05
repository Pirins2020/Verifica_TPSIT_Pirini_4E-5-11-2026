class Componente:
    def __init__(self, codice:str, nome:str, peso_kg: float) -> None :
        self.codice = codice
        self.nome = nome
        if peso_kg > 0 :
            self.peso_kg = peso_kg
            else :
                print("Il peso non può essere negativo")