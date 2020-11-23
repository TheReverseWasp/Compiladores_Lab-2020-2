import sys
sys.path.append("gramclasses")
from ExpresionTerminal import *
from ExpresionNoTerminal import *

from TASFinal import *



class Interprete:
    def __init__(self, TAS):
        self.gram = TAS.gram
        self.TAS = TAS
        self.funAL = TAS.funAL
        self.expresionTerminalMaestra = ExpresionTerminal("ETMaestra", [])

    def verificarExpresion(self, expr, tokens):
        itExpr = 0
        it = 0
        exprContent = []
        while itExpr < len(expr.prodList):
            if len(tokens) <= it:
                expresionTerminal = self.expresionTerminalMaestra.interpretarVacio("$")
            else:
                expresionTerminal = self.expresionTerminalMaestra.interpretar(tokens[it])
            prodList = False
            nombre = expr.prodList[itExpr]
            if expr.prodList[itExpr] in self.gram.noterminales:
                for i in self.gram.Producciones:
                    izq = i.izq
                    if izq == nombre and expresionTerminal.nombre in self.gram.getPrimero(izq):
                        # El token esta dentro de la producción
                        if i.der[0] in self.gram.terminales and i.der[0] == expresionTerminal.nombre:
                            prodList = i.der
                            break
                        elif i.der[0] in self.gram.noterminales:
                            prodList = i.der
                            break
                if not prodList:
                    # Compruebo si la expresion acepta vacios
                    prodList = self.gram.searchForEmpty(nombre)
                try:
                    expresionNoTerminal = ExpresionNoTerminal(nombre, prodList)
                    tempit, tempexpr = self.verificarExpresion(expresionNoTerminal, tokens[it:])
                    if tempit == False:
                        return False, False
                except:
                    print("Error: No hay gramatica disponible para esta expresión")
                    return False, False
                try:
                    it += tempit
                    itExpr += 1
                    expresionNoTerminal.interpretar(tempexpr)
                    exprContent.append(cp.deepcopy(expresionNoTerminal))
                except:
                    print("Error: Error en la producción")
                    return False, False
            elif expr.prodList[itExpr] in self.gram.terminales:
                if expr.prodList[itExpr] == "$":
                    exprContent.append(cp.deepcopy(self.expresionTerminalMaestra.interpretarVacio("$")))
                elif nombre == expresionTerminal.getNombre():
                    if not expresionTerminal.getNombre() == "$":
                        it += 1
                    exprContent.append(cp.deepcopy(expresionTerminal))
                else:
                    print("Error: La expresión recibio", expresionTerminal.getNombre(), "pero se esperaba", nombre)
                    return False, False
                itExpr += 1
            else:
                print("Error: Simbolo desconocido")
                return False, False

        return it, exprContent

    def verificarCorrectitud(self, linea, init_char):
        tokens = self.funAL(linea)
        if not tokens:
            print("Error: tokens incorrectos")
            return False
        for i in range(len(tokens)):
            print(i, end=" ")
            tokens[i].imprimir_token()
        unicaProduccion, prodUnica = self.gram.getProduccionUnica(init_char)
        if not unicaProduccion:
            print("Error: El char de inicio no tiene un solo valor unico")
            return False
        expr = ExpresionNoTerminal("E", prodUnica[0])
        it, items = self.verificarExpresion(expr, tokens)
        if not it:
            print("Error: en la gramatica")
            return False
        expr = expr.interpretar(items)
        if not expr:
            print("Error identificando los items")
            return False
        print("Gramatica Correcta")
        return expr
