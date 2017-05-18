
import math
from matplotlib import pyplot as plt
import collections
from random import randint

class TSP:
	
	""" Define os algoritmos para resolucao do TSP  """
	def __init__(self):
		pass
	
	# transforma a lista de cidades em uma matrix de custos
	def get_distance_matrix(self, cities):

		size = len(cities) + 1

		M = [ [0 for _ in range(size)] for __ in range(size) ]

		for i in cities:
			for j in cities:
				M[i.id][j.id] = self.distance(i, j)

		return M

	# imprime a matrix de custo de uma forma mais legivel
	def pretty_print(self, M):
		print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
	  for row in M]))

	# Calcula distancia ecludiana entre dois objectos cidade
	def distance(self, c1, c2):

		xd = c1.x - c2.x 
		yd = c1.y - c2.y 
		dij = int( math.sqrt( xd*xd + yd*yd) + 0.5 )

		return dij

	# retorna distancia entre 2 cidades
	def distance_by_matrix(self, c1, c2, M):
		return M[c1.id][c2.id]

	# retorna o vizinho mais proximo da cidade A, utilizando a matrix de distancias
	# como referencia
	def _nearest_neighbor(self, A, cities, M):
		
		min_d = float("inf")
		min_city = None
		for i in cities:
			if M[A.id][i.id] < min_d and M[A.id][i.id] > 0:
				min_d = M[A.id][i.id]
				min_city = i

		return min_city

	# algoritmo principal do nearest neighbor
	def nn_tsp(self, cities, M):

		startCity = cities.pop(0)

		# primeira cidade da rota sera a cidade na posicao [startIndex] do array
		tour = [startCity]
		unvisited = set(cities)

		while unvisited:
			lastVisitedCity = tour[-1]
			C = self._nearest_neighbor(lastVisitedCity, unvisited, M)
			tour.append(C)
			unvisited.remove(C)

		tour.append(startCity)

		return tour

	def greedy_tsp(self, cities):
		"""Go through edges, shortest first. Use edge to join segments if possible."""
		endpoints = {c: [c] for c in cities} # A dict of {endpoint: segment}
		
		startCity = cities.pop(0)
		path = None
		
		for (A, B) in self._shortest_edges_first(cities):
			if A in endpoints and B in endpoints and endpoints[A] != endpoints[B]:
				new_segment = self._join_endpoints(endpoints, A, B)
				if len(new_segment) == len(cities):
					path = new_segment
					break

		path.append(startCity)
		path = [startCity] + path

		return path

	def _shortest_edges_first(self,cities):
		
		# cria tuplas entre as cidades
		# 
		# Para nao repeticao de tuplas ex.(A,B) e (B,A)
		# 	uso o if id(A) < id(B) id = posicao na mem 'posicao na memoria'
		# 	
		edges = [(A, B) for A in cities for B in cities 
						if id(A) < id(B)]

		return sorted(edges, key=lambda edge: self.distance(*edge))
	
	def _join_endpoints(self,endpoints, A, B):
		"Join B's segment onto the end of A's and return the segment. Maintain endpoints dict."
		Asegment, Bsegment = endpoints[A], endpoints[B]
		if Asegment[-1] is not A: Asegment.reverse()
		if Bsegment[0] is not B: Bsegment.reverse()
		Asegment.extend(Bsegment)
		del endpoints[A], endpoints[B] # A and B are no longer endpoints
		endpoints[Asegment[0]] = endpoints[Asegment[-1]] = Asegment
		return Asegment

	def print_tour(self, cities):
		for i in cities:
			print (i)

	def print_tour_simple(self, cities):
		string = ""
		for i in cities:
			string += str(i.id) + " "

		print (string)

	def plot_cities(self, cities):
		fig = plt.figure()
		ax = fig.add_subplot(111)

		Xs = [ i.x for i in cities ]
		Ys = [ i.y for i in cities ]

		plt.scatter(Xs, Ys, marker='o', cmap=plt.get_cmap('Spectral'))
		plt.plot(Xs, Ys)
		
		for i in cities:                                    
			ax.annotate(i.id, [i.x, i.y], textcoords='data')
		
		plt.show()

	def get_cost(self, tour, M):
		
		deque_cities = collections.deque(tour)

		total_cost = 0

		current_city = deque_cities.popleft()

		while len(deque_cities):
			next_city = deque_cities.popleft()
			total_cost += self.distance_by_matrix(current_city, next_city, M)

			current_city = next_city

		return total_cost

	def _swap(self, tour, i1, i2):
		clone = tour[:]

		aux = clone[i1]
		clone[i1] = clone[i2]
		clone[i2] = aux

		return clone

	# aplica a _swap em elementos aleatorios em busca 
	# de um tour menor, NAO PODE MUDAR NEN A ORIGEM NEN O DESTINO !
	def swap_2opt(self, tour, M, number_of_tries):

		min_cost = self.get_cost(tour, M)
		min_tour = tour[:]

		size = len(tour)

		for i in range(number_of_tries):
			r1 = randint(1, size - 2)
			r2 = randint(1, size - 2)

			new_tour = self._swap(min_tour, r1, r2)
			new_cost = self.get_cost(new_tour, M)

			if new_cost < min_cost:
				print ("FOUND !")
				min_cost = new_cost
				min_tour = new_tour

		return min_tour

	def swap_3opt(self, tour, M, number_of_tries):

		min_cost = self.get_cost(tour, M)
		min_tour = tour[:]

		size = len(tour)

		for i in range(number_of_tries):
			r1 = randint(1, size - 2)
			r2 = randint(1, size - 2)
			r3 = randint(1, size - 2)

			new_tour = self._swap(min_tour, r1, r2)
			new_tour2 = self._swap(new_tour, r2, r3)

			new_cost = self.get_cost(new_tour2, M)

			if new_cost < min_cost:
				print ("FOUND !")
				min_cost = new_cost
				min_tour = new_tour

		return min_tour








"""
	mOv visinhanca

	Movimentos em cima do resultado (2opt, 3opt, ...)

	VND 
		-> Manipular os movimentos varias vezes para encontrar uma sol melhor
"""

















		