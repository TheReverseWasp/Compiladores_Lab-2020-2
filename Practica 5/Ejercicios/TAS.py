from Gram import *

class TAS_Prac4:
    def __init__(self, gram, funAL):
        self.gram = gram
        self.funAL = funAL
        #Modificar para otras gramaticas a paartir de aqui
        self.start = "E"
        self.TAS = {}
        #E
        self.TAS["E"] = {}
        self.TAS["E"]["("] = Produccion("E", ["T", "Ep"])
        self.TAS["E"]["Numero"] = Produccion("E", ["T", "Ep"])
        self.TAS["E"]["id"] = Produccion("E", ["T", "Ep"])
        #Ep
        self.TAS["Ep"] = {}
        self.TAS["Ep"]["+"] = Produccion("Ep", ["+", "T", "Ep"])
        self.TAS["Ep"]["-"] = Produccion("Ep", ["-", "T", "Ep"])
        self.TAS["Ep"][")"] = Produccion("Ep", ["$"])
        self.TAS["Ep"]["$"] = Produccion("Ep", ["$"])
        #T
        self.TAS["T"] = {}
        self.TAS["T"]["("] = Produccion("T", ["F", "Tp"])
        self.TAS["T"]["Numero"] = Produccion("T", ["F", "Tp"])
        self.TAS["T"]["id"] = Produccion("T", ["F", "Tp"])
        #Tp
        self.TAS["Tp"] = {}
        self.TAS["Tp"]["+"] = Produccion("Tp", ["$"])
        self.TAS["Tp"]["-"] = Produccion("Tp", ["$"])
        self.TAS["Tp"]["*"] = Produccion("Tp", ["*", "F", "Tp"])
        self.TAS["Tp"]["/"] = Produccion("Tp", ["/", "F", "Tp"])
        self.TAS["Tp"][")"] = Produccion("Tp", ["$"])
        self.TAS["Tp"]["$"] = Produccion("Tp", ["$"])
        #F
        self.TAS["F"] = {}
        self.TAS["F"]["("] = Produccion("F", ["(", "E", ")"])
        self.TAS["F"]["Numero"] = Produccion("F", ["Numero"])
        self.TAS["F"]["id"] = Produccion("F", ["id"])

    def check_if_correct(self, texto):
        tokens = self.funAL(texto)
        if tokens != False:
            #then check
            it = 0
            nsit = 0
            ns = self.start
            q = []
            while nsit < len(tokens):
                print(it, "E -> ", end="")
                if tokens[nsit].tipo == "Numero" or tokens[nsit].tipo == "id":
                    val = tokens[nsit].tipo
                else:
                    val = tokens[nsit].palabra
                if it == 0:
                    if val in self.TAS[ns]:
                        #replace
                        q.append(self.TAS[ns][val].der)
                        q = flatten(q)
                    else:
                        print("Error en la gramatica")
                        return False
                else:
                    if val in self.TAS[ns]:
                        #replace
                        if self.TAS[ns][val].der[0] != "$":
                            q[nsit] = self.TAS[ns][val].der
                        else:
                            q[nsit] = []
                        q = flatten(q)
                    else:
                        print("Error en la gramatica")
                        return False
                if q[nsit] in self.gram.terminales:
                    #Go Ahead
                    nsit += 1
                else:
                    ns = q[nsit]
                print(str(q))
                ns = q[nsit]
                it += 1
            val = "$"
            while len(q) != len(tokens):
                ns = q[nsit]
                print(it, "E -> ", end="")
                if val in self.TAS[ns]:
                    if self.TAS[ns][val].der[0] != "$":
                        q[nsit] = self.TAS[ns][val].der
                    else:
                        q[nsit] = []
                    q = flatten(q)
                else:
                    print("Error en la gramatica")
                    return False
                print(str(q))
                it += 1
        print("Gramatica Correcta")
        return True
