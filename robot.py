import Componente.py
class Robot:
    def __init__(self, codice: str, modello: str, applicazione: str, peso_massimo_componenti_kg: float, stato: str) -> None :
        self.codice = codice
        self.modello = modello
        self.applicazione = applicazione
        sel.peso_massimo_componenti_kg = peso_massimo_componenti_kg
        self.stato = stato
    
    componenti = []
    
    
    def aggiungi_componente (componente: Componente()) -> None :
        pesoTot = 0
        id = componente.codice
        for comp in componenti :
            pesoTot = pesoTot + comp.peso_kg
            if pesoTot > peso_massimo_componenti_kg :
                print ("Componente rifiutato, peso troppo elevato")
            else :
                for i in componenti :
                    if id == i.codice :
                        print("Componente rifiutato, codice già presente")
                    else :
                        componenti.append(componente)
    
    def peso_componenti () -> float :
        somma = 0
        for i in componenti:
            somma = somma + i.peso_kg
        return somma
    
    def cerca_componente (codice:  str) -> Componente :
        componenteDaTrovare = Componente
        for i in componenti:
            if codice == i.codice :
                componenteDaTrovare = i
        return componenteDaTrovare
    
    def rimuovi_componente (codice:  str) -> Componente :
        componenteDaTrovare = Componente
        for i in componenti:
            if codice == i.codice :
                componenteDaTrovare = i
                componenti.remove(i)
        return componenteDaTrovare
    
    def componenti_sotto_peso (peso_massimo: float) -> list[Componente] :
        componenti_sotto_peso = []
        for i in componenti:
            if i.peso_kg < peso_massimo :
                componenti_sotto_peso.append(i)
        return componenti_sotto_peso
                
    
    
    
    
    
            
                        
                
            