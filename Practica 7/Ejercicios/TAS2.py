from Gram import *


class TAS_Dynamic_P6:
    def __init__(self, gram, funAL):
        self.gram = gram
        self.funAL = funAL
        #Modificar para otras gramaticas a paartir de aqui
        self.start = "E"
        self.TAS = {}

    def crear_tabla(self):
        for k1, v1 in self.gram.noterminales.items():
            self.TAS[k1] = {}
            primeros = self.gram.getPrimero(k1)
            for i in primeros:
                for j in self.gram.Producciones:
                    if j.izq == k1:
                        h_primeros = self.gram.getPrimero(j.der[0])
                        if i in h_primeros:
                            self.TAS[k1][i] = j

    def imprimir_TAS(self):
        for k1, v1 in self.TAS.items():
            print(k1)
            for k2, v2 in v1.items():
                print("[+] " + k2 + " : " + v2.izq + " -> " + str(v2.der))



    def check_if_correct(self, texto):
        tokens = self.funAL(texto)
        for i in tokens:
            if i.tipo in byTipo:
                print(i.tipo, end=" ")
            else:
                print(i.palabra, end=" ")
        print()
        if tokens != False:
            #then check
            it = 0
            nsit = 0
            ns = self.start
            q = []
            while nsit < len(tokens):
                print(it, "E -> ",  end="")
                if tokens[nsit].tipo in byTipo:
                    val = tokens[nsit].tipo
                else:
                    val = tokens[nsit].palabra
                if len(q) == 0:
                    if val in self.TAS[ns]:
                        #replace
                        q.append(self.TAS[ns][val].der)
                        q = flatten(q)
                    else:
                        if "$" in self.TAS[ns]:
                            q.append(self.TAS[ns]["$"].der)
                            q = flatten(q)
                        else:
                            print("Error en la gramatica")
                            return False
                elif q[nsit] in self.gram.noterminales:
                    if val in self.TAS[ns]:
                        #replace
                        q[nsit] = self.TAS[ns][val].der
                        q = flatten(q)
                    else:
                        if "$" in self.TAS[ns]:
                            q[nsit] = self.TAS[ns]["$"].der
                            q = flatten(q)
                        else:
                            print("Error en la gramatica")
                            return False
                if q[nsit] in self.gram.terminales:
                    #Go Ahead
                    if q[nsit] == "$":
                        q[nsit] = []
                        q = flatten(q)
                        nsit -= 1
                    nsit += 1
                if nsit < len(q):
                    ns = q[nsit]
                print(str(q))
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
        else:
            print("Error al identificar tokens")
            return False
        print("Gramatica Correcta")
        return True
