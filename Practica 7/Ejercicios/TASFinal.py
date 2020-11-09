from Gram import *
import sys
sys.path.append("gramclasses")
from ExpresionNoTerminal import *
from ExpresionTerminal import *

class Interprete:
	def __init__(self, gram, funAL):
		self.gram = gram
		self.funAL = funAL
        #Modificar para otras gramaticas a paartir de aqui
		self.start = "E"
		self.TAS = {}
		self.expresionTerminalMaestra = ExpresionTerminal("ETMaestra")
		self.expresionNoTerminalMaestra = ExpresionNoTerminal("ETMaestra")

	def crear_tabla(self):
		for k1, v1 in self.gram.noterminales.items():
			self.TAS[k1] = cp.deepcopy(self.expresionNoTerminalMaestra)
			self.TAS[k1].setNombre(k1)
			primeros = self.gram.getPrimero(k1)
			for i in primeros:
				for j in self.gram.Producciones:
					if j.izq == k1:
						h_primeros = self.gram.getPrimero(j.der[0])
						if i in h_primeros:
							self.TAS[k1].addCamino(i, j.der)

	def imprimir_tas(self):
		for k, v in self.TAS.items():
			print(k)
			v.imprimirExpresion()

	def verificar_expresion(self, expr, tokens):
		it = 0
		exprit = 0
		items = []
		print(expr)
		if len(tokens) == 0:
			expresionTerminal = self.expresionTerminalMaestra.interpretarVacio("$")
		else:
			expresionTerminal = self.expresionTerminalMaestra.interpretar(tokens[it])
		for key, values in self.TAS[expr].caminos.items():
			primeros = self.gram.getPrimero(values[0])
			if expresionTerminal.getNombre() in primeros or "$" in primeros:
				v = values
				break
			else:
				v = False
		if not v:
			print("Error en la gramatica: No se pudo parsear la expresion")
			return False, False
		while it < len(tokens) and exprit < len(v):
			print(it, exprit, tokens[it].palabra)
			print(expr, v)
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

