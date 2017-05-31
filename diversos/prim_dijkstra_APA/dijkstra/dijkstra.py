# Trabalho DIJKSTRA
# 
# Aluno 	 : Igor Leal Antunes (11211416) e Fernando Souza (11218354)
# Disciplina : Analise e Projeto de Algoritmos - 2016.2
# Professor  : GILBERTO FARIAS DE SOUSA FILHO 
#
#
# uso : 
# 		utilizando pipe de arquivo:
# 			> python dijkstra.py < nome_do_arquivo
# 
# 		ou
#		
#		Digitando a entrada direto no console
#		
#			> python dijkstra.py
#			> 9
#			> 4 0 0 0 0 0 8 0
#			> 8 0 0 0 0 11 0
#			> 7 0 4 0 0 2
#			> 9 14 0 0 0
#			> 10 0 0 0
#			> 2 0 0
#			> 1 6
#			> 7


import numpy as np
import sys
from min_heap import Min_heap
from min_heap import Heap_obj

n = int(input())

matrix = []

for i in range(1, n): # popula triangulo superior direito
	matrix.append( [ 0 for _ in xrange(0, i) ] + list(map(int, raw_input().split())) )

matrix.append( [ 0 for _ in xrange(0, n) ]) # escreve ultima linha de zeros

# transforma numa matrix cheia
for i in xrange(0, n):
	for j in xrange(0, n):
		matrix[j][i] = matrix[i][j]

lista = {}
# controi a lista de adjacencia
for i in xrange(1, n+1):
	lista[i] = []
	for j in xrange(1, n+1):
		if matrix[i-1][j-1] != 0:
			lista[i].append(j)


heap = Min_heap()
heap.build_heap([ Heap_obj(0, 1) ] + [ Heap_obj(sys.maxint, i) for i in range(2,n+1)])

#heap.print_heap()

fathers_map = {}
costs_map   = {}

#print '\n'.join([' '.join(str(row)) for row in matrix])

while len(heap.list) > 1:

	heap.fix_down(1)
	u = heap.pop_min()

	#print ""
	#heap.print_heap()
	#print ""
	# atualiza mapa de custo para a origem
	costs_map[u.k] = u.v

	for v in lista[u.k]: # para cada el adjacente

		m_v = matrix[u.k-1][v-1] # custo desse elemento para o atual

		if heap.contains(v) and (u.v + m_v) < heap.list[heap.map[v]].v: 
			
			heap.list[heap.map[v]].v = u.v + m_v
			fathers_map[v] = u.k # atualiza pai


# Anda no mapa de pais ao contrario para chegar na origem
caminho = []
atual = n
while atual > 1: # enquanto nao chega na origem => refaz o caminho
	caminho.append(atual)
	atual = fathers_map[atual]

print "CAMINHO : "
print [1] + caminho[::-1]
print "CUSTO : "
print costs_map[n] # acha o custo para o ultimo elemento

#print fathers_map
#print costs_map




























