
from City import City
from TSP import TSP

import random
import time
import itertools
import urllib
import csv
import functools

def main():
		
	cities = []

	while True:
		try:
			line = input().strip()

			if line == "NODE_COORD_SECTION":
			   
				while True:
					try:
						
						line = input().split()
						city = City(line[0], line[1], line[2])
						cities.append(city)
					except Exception as e:
						#print ("1 " + str(e))
						break;

		except Exception as e:
			#print ("2 " + str(e))
			break;
	
	
	"""
	#A => C : 1.41421
	#C => D : 5 
	#D => B : 3.16228
	#B => A : 8.06226
	
	cities_2 = [ 
				  City("A", 1, 2), 
				  City("B", 5, 9),
				  City("C", 2, 3),
				  City("D", 6, 6)  
				]

	tsp = TSP()
	
	tour_nn = tsp.nn_tsp(cities_2[:])
	tour_greedy = tsp.greedy_tsp(cities_2[:])
	tsp.print_tour(tour_nn)
	
	print( "\nCusto Total: tour_nn " + str(tsp.get_cost(tour_nn)))
	print( "\nCusto Total: tour_greedy " + str(tsp.get_cost(tour_greedy)))
	"""

	
	tsp = TSP()
	tour_nn = tsp.nn_tsp(cities[:])
	tour_greedy = tsp.greedy_tsp(cities[:])

	tsp.print_tour(tour_nn)
	print("\n")
	tsp.print_tour(tour_greedy)

	print( "\nCusto Total: tour_nn " + str(tsp.get_cost(tour_nn)))
	print( "\nCusto Total: tour_greedy " + str(tsp.get_cost(tour_greedy)))
	
main()













