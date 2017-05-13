
import math
from matplotlib import pyplot as plt
import collections

class TSP:
	
	""" Define os algoritmos para resolucao do TSP  """
	def __init__(self):
		pass
			
	def distance(self, c1, c2):

		xd = c1.x - c2.x 
		yd = c1.y - c2.y 
		dij = int( math.sqrt( xd*xd + yd*yd) + 0.5 )

		return dij

	def _nearest_neighbor(self, A, cities):
		# Calcula a distancia de A => todas as cidades em cities e retorna a minima
		return min(cities, key=lambda c: self.distance(c, A))

	def nn_tsp(self, cities, startIndex = 0):
		"""Start the tour at the first city; at each step extend the tour 
		by moving from the previous city to the nearest neighboring city, C,
		that has not yet been visited."""

		startCity = cities.pop(startIndex)

		# primeira cidade da rota sera a cidade na posicao [startIndex] do array
		tour = [startCity]
		unvisited = set(cities)

		while unvisited:
			lastVisitedCity = tour[-1]
			C = self._nearest_neighbor(lastVisitedCity, unvisited)
			tour.append(C)
			unvisited.remove(C)

		tour.append(startCity)

		return tour

	def greedy_tsp(self, cities, startIndex = 0):
		"""Go through edges, shortest first. Use edge to join segments if possible."""
		endpoints = {c: [c] for c in cities} # A dict of {endpoint: segment}
		
		startCity = cities.pop(startIndex)
		path = None
		
		for (A, B) in self.shortest_edges_first(cities):
			if A in endpoints and B in endpoints and endpoints[A] != endpoints[B]:
				new_segment = self.join_endpoints(endpoints, A, B)
				if len(new_segment) == len(cities):
					path = new_segment
					break

		path.append(startCity)
		path = [startCity] + path

		return path

	def shortest_edges_first(self,cities):
		"Return all edges between distinct cities, sorted shortest first."
		
		# cria tuplas entre as cidades
		# 
		# Para nao repeticao de tuplas ex.(A,B) e (B,A)
		# 	uso o if id(A) < id(B) id = posicao na mem 'posicao na memoria'
		# 	
		edges = [(A, B) for A in cities for B in cities 
						if id(A) < id(B)]

		return sorted(edges, key=lambda edge: self.distance(*edge))
	
	def join_endpoints(self,endpoints, A, B):
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

	def plot_cities(self, cities):
		fig = plt.figure()
		ax = fig.add_subplot(111)

		Xs = [ i.x for i in cities ]
		Ys = [ i.y for i in cities ]

		plt.scatter(Xs, Ys, marker='o', cmap=plt.get_cmap('Spectral'))
		
		for i in cities:                                    
			ax.annotate(i.id, [i.x, i.y], textcoords='data')
		
		plt.show()

	def get_cost(self, cities):
		
		deque_cities = collections.deque(cities)

		total_cost = 0

		current_city = deque_cities.popleft()

		while len(deque_cities):
			next_city = deque_cities.popleft()
			total_cost += self.distance(current_city, next_city)

			current_city = next_city

		return total_cost













		