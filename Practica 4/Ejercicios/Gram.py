from AL import *

class Produccion:
    def __init__(self, izq, der):
        self.izq = izq
        self.der = der

class Gram_Prac4:
    def __init__(self):
        noterm_operadores = ["+", "-", "*", "/"]
        self.Producciones = []
        self.terminales = {}
        self.noterminales = {}
        #Terminales
        for i in noterm_operadores:
            self.terminales[i] = i
        self.terminales["id"] = "id"
        self.terminales["Numero"] = "Numero"
        self.terminales["("] = "("
        self.terminales[")"] = ")"
        self.terminales["EOS"] = "EOS"
        #No Terminales
        self.noterminales["E"] = "E"
        self.noterminales["Ep"] = "Ep"
        self.noterminales["T"] = "T"
        self.noterminales["Tp"] = "Tp"
        self.noterminales["F"] = "F"
        #Producciones
        self.Producciones.append(Produccion("E", ["T", "Ep"]))
        self.Producciones.append(Produccion("Ep", ["+", "T", "Ep"]))
        self.Producciones.append(Produccion("Ep", ["+", "T", "Ep"]))
        self.Producciones.append(Produccion("Ep", ["EOS"]))
        self.Producciones.append(Produccion("T", ["F", "Tp"]))
        self.Producciones.append(Produccion("Tp", ["*", "F", "Tp"]))
        self.Producciones.append(Produccion("Tp", ["/", "F", "Tp"]))
        self.Producciones.append(Produccion("Tp", ["EOS"]))
        self.Producciones.append(Produccion("F", ["(", "E", ")"]))
        self.Producciones.append(Produccion("F", ["Numero"]))
        self.Producciones.append(Produccion("F", ["id"]))
