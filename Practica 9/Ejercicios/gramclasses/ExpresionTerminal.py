import sys
sys.path.append(".")
from ExpresionAbstracta import *

class ExpresionTerminal(ExpresionAbstracta):
	def interpretar(self, token):
		expresionTerminal = cp.deepcopy(self)
		expresionTerminal.nombre = token.tipo if token.tipo in byTipo else token.palabra
		expresionTerminal.expresion.append(token)
		return expresionTerminal

	def interpretarVacio(self, voidchar):
		expresionTerminal = cp.deepcopy(self)
		expresionTerminal.nombre = voidchar
		expresionTerminal.expresion.append(voidchar)
		return expresionTerminal

	def imprimirExpresionInterpretada(self):
		print(self.nombre)
