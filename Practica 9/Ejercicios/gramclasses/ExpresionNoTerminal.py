import sys
sys.path.append(".")
from ExpresionAbstracta import *

class ExpresionNoTerminal(ExpresionAbstracta):
	def interpretar(self, items):
		try:
			for i in range(len(items)):
				if self.prodList[i] == items[i].getNombre():
					self.expresion.append(items[i])
				else:
					print("Error: Los tokens no corresponden a la expresion:", self.prodList)
					return False
		except:
			print("Error: El numero de items de la expresion excede el de las producciones aceptadas.")
			return False
		if len(self.expresion) == len(items):
			return self
		return False

	def imprimirExpresionInterpretada(self):
		print(self.nombre, end=" -> ")
		for i in self.expresion:
			print(i.nombre, end=", ")
		print()
		for i in self.expresion:
			i.imprimirExpresionInterpretada()
