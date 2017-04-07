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

heap.print_heap()

fathers_map = {}
costs_map   = {}

print '\n'.join([' '.join(str(row)) for row in matrix])

while len(heap.list) > 1:

	heap.fix_down(1)
	u = heap.pop_min()

	# atualiza mapa de custo para a origem
	costs_map[u.k] = u.v

	for v in lista[u.k]:# para cada el adjacente

		m_v = matrix[u.k-1][v-1] # custo desse elemento para o atual

		if heap.contains(v) and (u.v + m_v) < heap.list[heap.map[v]].v: 
			
			heap.list[heap.map[v]].v = u.v + m_v
			fathers_map[v] = u.k # atualiza pai



print fathers_map
print costs_map




























