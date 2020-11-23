import sys
sys.path.append(".")
import copy as cp

byTipo = {"String": True, "id": True, "Numero": True}

class ProdNT:
	def __init__(self, nombre):
		self.nombre = nombre
		self.caminos = {}

	def setNombre(self, nombre):
		self.nombre = nombre

	def addCamino(self, key, der):
		self.caminos[key] = der
		return self.caminos[key]

	def getCaminos(self):
		caminos = [[k,v] for k,v in self.caminos.items()]
		return caminos

	def getNombre(self):
		return self.nombre

	def imprimirExpresion(self):
		print(self.nombre)
		for k, v in self.caminos.items():
			print("[+] " + k + " -> " + str(v))
