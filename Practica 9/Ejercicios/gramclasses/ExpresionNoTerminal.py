import sys
sys.path.append(".")
from ExpresionAbstracta import *

class ExpresionNoTerminal(ExpresionAbstracta):
	def interpretar(self, items):
		caminos = self.caminos[items[0].getPrimero()]
		expresionNoTerminal = cp.deepcopy(self)
		for i in range(0, min(len(caminos), len(items))):
			expresionNoTerminal.expresion.append(items[i])
		if not len(expresionNoTerminal.expresion) == len(caminos):
			return False
		return expresionNoTerminal

	def imprimirExpresionInterpretada(self):
		print(self.nombre, end=" -> ")
		for i in self.expresion:
			print(i.getNombre(), end=", ")
		print()
		for i in self.expresion:
			i.imprimirExpresionInterpretada()
