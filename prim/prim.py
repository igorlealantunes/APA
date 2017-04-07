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

path_map = {}
final_path = []

print '\n'.join([' '.join(str(row)) for row in matrix])

while len(heap.list) > 1:

	heap.fix_down(1)
	u = heap.pop_min()
	
	if u.k in path_map:
		final_path.append(path_map[u.k])

	for v in lista[u.k]:

		m_v = matrix[u.k-1][v-1]

		if heap.contains(v) and m_v < heap.list[heap.map[v]].v: 
			
			heap.list[heap.map[v]].v = m_v
			print "Adding to map " + str(v) + " : " +  str(u.k) + "->" +str(v)
			path_map[v] = str(u.k) + "->" +str(v)

			print ""
			heap.print_heap()

		
for i in final_path:
	print i
#print '\n'.join([' '.join(str(row)) for row in matrix])
