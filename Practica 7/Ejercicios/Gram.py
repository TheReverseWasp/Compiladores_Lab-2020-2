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
        self.terminales["$"] = "$"
        #No Terminales
        self.noterminales["E"] = "E"
        self.noterminales["Ep"] = "Ep"
        self.noterminales["T"] = "T"
        self.noterminales["Tp"] = "Tp"
        self.noterminales["F"] = "F"
        #Producciones
        self.Producciones.append(Produccion("E", ["T", "Ep"]))
        self.Producciones.append(Produccion("Ep", ["+", "T", "Ep"]))
        self.Producciones.append(Produccion("Ep", ["-", "T", "Ep"]))
        self.Producciones.append(Produccion("Ep", ["$"]))
        self.Producciones.append(Produccion("T", ["F", "Tp"]))
        self.Producciones.append(Produccion("Tp", ["*", "F", "Tp"]))
        self.Producciones.append(Produccion("Tp", ["/", "F", "Tp"]))
        self.Producciones.append(Produccion("Tp", ["$"]))
        self.Producciones.append(Produccion("F", ["(", "E", ")"]))
        self.Producciones.append(Produccion("F", ["Numero"]))
        self.Producciones.append(Produccion("F", ["id"]))

    def getProducciones(self):
        return self.Producciones

    def getPrimero(self, k, rec = False):
        if k in self.terminales:
            return [k]
        if k == rec:
            return False
        answer = []
        for p in self.Producciones:
            if k == p.izq:
                if p.der[0] in self.terminales:
                    answer.append(p.der[0])
                else:
                    answer.append(self.getPrimero(p.der[0], rec = k))
        answer = flatten(answer)
        a = {}
        for i in answer:
            a[i] = True
        answer = []
        for k, v in a.items():
            answer.append(k)
        return answer

    def getPrimeros(self):
        answer = []
        for k, v in self.noterminales.items():
            answer.append([k, self.getPrimero(k)])
        return answer
