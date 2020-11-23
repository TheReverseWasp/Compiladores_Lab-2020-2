import copy as cp

byTipo = {"String": True, "id": True, "Numero": True}

class ExpresionAbstracta:
	def __init__(self, nombre prodList):
		self.nombre = nombre
		self.prodList = []
		self.caminos = {}
		self.expresion = []

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

	def getPrimero(self):
		if len(self.expresion) > 0:
			if isinstance(self.expresion[0], ExpresionAbstracta):
				return self.expresion[0].getPrimero()
			else:
				w = self.expresion[0]
				return w.tipo if w.tipo in byTipo else w.palabra

	def imprimirExpresion(self):
		print(self.nombre)
		for k, v in self.caminos.items():
			print("[+] " + k + " -> " + str(v))
