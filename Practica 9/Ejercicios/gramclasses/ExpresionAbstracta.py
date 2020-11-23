import copy as cp

byTipo = {"String": True, "id": True, "Numero": True}

class ExpresionAbstracta:
	def __init__(self, nombre, prodList):
		self.nombre = nombre
		self.prodList = prodList
		self.expresion = []

	def setNombre(self, nombre):
		self.nombre = nombre

	def getNombre(self):
		return self.nombre
