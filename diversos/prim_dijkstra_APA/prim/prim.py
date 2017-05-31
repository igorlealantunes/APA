
#
# Trabalho PRIM
# 
# Aluno 	 : Igor Leal Antunes (11211416) e Fernando Souza (11218354)
# Disciplina : Analise e Projeto de Algoritmos - 2016.2
# Professor  : GILBERTO FARIAS DE SOUSA FILHO 
#
#
# uso : 
# 		utilizando pipe de arquivo:
# 			> python prim.py < nome_do_arquivo
# 
# 		ou
#		
#		Digitando a entrada direto no console
#		
#			> python prim.py
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

path_map = {}
final_path = []

#print '\n'.join([' '.join(str(row)) for row in matrix])

total_cost = 0

while len(heap.list) > 1:

	heap.fix_down(1)
	u = heap.pop_min()
	
	if u.k in path_map:
		final_path.append(path_map[u.k])
		total_cost += u.v

	for v in lista[u.k]:

		m_v = matrix[u.k-1][v-1]

		if heap.contains(v) and m_v < heap.list[heap.map[v]].v: 
			
			heap.list[heap.map[v]].v = m_v
			#print "Adding to map " + str(v) + " : " +  str(u.k) + "->" +str(v)
			path_map[v] = str(u.k) + "->" +str(v)

			#print ""
			#heap.print_heap()

	
print "Ligacoes : "	
for i in final_path:
	print i

print "Custo total : " + str(total_cost)

#print '\n'.join([' '.join(str(row)) for row in matrix])
