from Gram import *
import sys
sys.path.append("gramclasses")

from ProdNT import *

class TASMaestra:
	def __init__(self, gram, funAL):
		self.gram = gram
		self.funAL = funAL
        #Modificar para otras gramaticas a paartir de aqui
		self.start = "E"
		self.TAS = {}
		self.prodNoTerminal = ProdNT("PNTMaestra")

	def crearTabla(self):
		for k1, v1 in self.gram.noterminales.items():
			self.TAS[k1] = cp.deepcopy(self.prodNoTerminal)
			self.TAS[k1].setNombre(k1)
			primeros = self.gram.getPrimero(k1)
			for i in primeros:
				for j in self.gram.Producciones:
					if j.izq == k1:
						h_primeros = self.gram.getPrimero(j.der[0])
						if i in h_primeros:
							self.TAS[k1].addCamino(i, j.der)

	def imprimirTAS(self):
		for k, v in self.TAS.items():
			print(k, end=", ")
		print()
		for k, v in self.TAS.items():
			v.imprimirExpresion()
