#
# Trabalho Final
# 
# Aluno      : Igor Leal Antunes (11211416) e Fernando Souza (11218354)
# Disciplina : Analise e Projeto de Algoritmos - 2016.2
# Professor  : GILBERTO FARIAS DE SOUSA FILHO 


class City:
	
	"""Define cada no' no TSP
	
		ID : Identificador da cidade (nome)
		x  : latitude no mapa
		y  : longitude no mapa
	"""
	
	def __init__(self, id, x, y):
		self.id = int(id)
		self.x = float(x)
		self.y = float(y)

	def to_string(self):
		return str(self.id) + ": " + str(self.x) + " " + str(self.y)
	
	def __str__(self):
		return self.to_string()
		

		