#
# Trabalho Final
# 
# Aluno      : Igor Leal Antunes (11211416) e Fernando Souza (11218354)
# Disciplina : Analise e Projeto de Algoritmos - 2016.2
# Professor  : GILBERTO FARIAS DE SOUSA FILHO 
#
#
# uso : 
#       utilizando pipe de arquivo:
#           > python3 app.py < nome_do_arquivo.txt
#           
#           
from City import City
from TSP import TSP

import random
import time
import itertools
import urllib
import csv
import functools
import pprint 
	
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
						#print ("1 " + str(e) + " city :" + str(city.id))
						break;

		except Exception as e:
			#print ("2 " + str(e) + " city :" + str(city.id))
			break;
	
	tsp = TSP()
	M = tsp.get_distance_matrix(cities)
	
	# GRASP
	custo_original = tsp.get_cost(cities, M)

	nn_tour = tsp.nn_tsp(cities, M)
	custo_nn = tsp.get_cost(nn_tour, M)

	#print ("\nCusto NN : " + str(custo_nn))
	#tsp.print_tour_simple(nn_tour)

	minimo = float("inf")

	for i in range(1000000):
		alpha = random.uniform(0, 1)
		grasp_tour = tsp.GRASP_TSP(cities, M, alpha)
		custo_final = tsp.get_cost(grasp_tour, M)

		if custo_final < minimo:
			print ("\nAlpha : " + str(alpha) + " Custo GRASP: " + str(custo_final))
			tsp.plot_cities(grasp_tour)
			minimo = custo_final


	#tsp.print_tour_simple(grasp_tour)

	#tsp.plot_cities(grasp_tour)


	#melhora = (1 - (custo_final / custo_original)) * 100.0

	#print("\nCusto Original (com vizinho mais proximo): " + str(custo_original))
	#tsp.print_tour_simple(tour)
	#print("Custo Otimizado pelo VND: " + str(custo_final)) 
	#print("Melhora : " + str(melhora) + " %")

	#tsp.print_tour_simple(new_tour)

	#tsp.plot_cities(tour)
	#tsp.plot_cities(new_tour)
	
	######### http://mauricio.resende.info/talks/grasp-ecco2000.pdf



main()



