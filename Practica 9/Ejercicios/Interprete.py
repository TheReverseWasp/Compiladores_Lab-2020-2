from TASFFinal import *

class Interprete:
    def __init__(self, TAS, Gram):
        self.Gram = Gram
        self.TAS = TAS
		self.expresionTerminalMaestra = ExpresionTerminal("ETMaestra", [])
		self.expresionNoTerminalMaestra = ExpresionNoTerminal("ETMaestra", [])

	def verificarExpresion(self, expr, tokens):
        itExpr = 0
        it = 0:
        while itExpr < len(expr.prodList):
            if len(tokens) == it:
                expresionTerminal = self.expresionTerminalMaestra.interpretarVacio("$")
    		else:
    			expresionTerminal = self.expresionTerminalMaestra.interpretar(tokens[it])

            prodList = false
            if expr.prodList[itExpr] in self.Gram.noterminales:
                nombre = expr.prodList[itExpr]
                for i in self.Gram:
                    izq = i.Producciones.izq
                    if izq == nombre and expresionTerminal.nombre in self.Gram.getPrimero(izq):
                        # El token esta dentro de la producción
                        prodList = i.Producciones.der
                        break
                try:
                    expresionNoTerminal = ExpresionNoTerminal(nombre, prodList)
                except e:
                    print("Error: No hay gramatica disponible para esta expresión")
                it,  self.verificarExpresion(expresionNoTerminal, tokens[it:])


        if not v:
			print("Error en la gramatica: No se pudo parsear la expresion")
			return False, False
		while it < len(tokens) and exprit < len(v):
			elem = v[exprit]
			if elem in self.gram.terminales:
				if elem in self.gram.terminales:
					if elem != "$":
						expresionTerminal = self.expresionTerminalMaestra.interpretar(tokens[it])
						items.append(expresionTerminal)
						it += 1
						exprit += 1
					else:
						expresionTerminal = self.expresionTerminalMaestra.interpretarVacio("$")
						items.append(expresionTerminal)
						exprit += 1
				else:
					tempit, tempExpresionNoTerminal = verificar_expresion(elem, tokens[it:])
					if not tempExpresionNoTerminal:
						print("error 1")
						return False, False
					expresionNoTerminal = self.TAS[elem].interpretar(tempExpresionNoTerminal)
					items.append(expresionNoTerminal)
					it += tempit
					exprit += 1
			else:
				tempit, tempExpresionNoTerminal = self.verificar_expresion(elem, tokens[it:])
				if not tempExpresionNoTerminal:
					print("error 2")
					return False, False
				expresionNoTerminal = self.TAS[elem].interpretar(tempExpresionNoTerminal)
				items.append(expresionNoTerminal)
				it += tempit
				exprit += 1
		while exprit < len(v):
			if v[exprit] == "$":
				expresionTerminal = self.expresionTerminalMaestra.interpretarVacio("$")
				items.append(expresionTerminal)
				exprit += 1
			else:
				if v[exprit] in self.gram.terminales:
					print("error 3")
					return False, False
				else:
					tempit, tempExpresionNoTerminal = self.verificar_expresion(v[exprit], tokens[it:])
					if not tempExpresionNoTerminal:
						print("error 4")
						return False, False
					expresionNoTerminal = self.TAS[v[exprit]].interpretar(tempExpresionNoTerminal)
					items.append(expresionNoTerminal)
					it += tempit
					exprit += 1
		return it, items

	def verificar_correctitud(self, linea):
		tokens = self.funAL(linea)
		print(tokens)
		if not tokens:
			print("Error: tokens incorrectos")
			return False
		for i in range(len(tokens)):
			print(i, end=" ")
			tokens[i].imprimir_token()
		it, items = self.verificar_expresion(self.start, tokens)
		if not items:
			print("Error en la gramatica")
			return False
		print(items)
		expresionNoTerminal = self.TAS[self.start].interpretar(items)
		if not expresionNoTerminal:
			print("Error identificando los items")
			return False
		print("Gramatica Correcta")
		return expresionNoTerminal
