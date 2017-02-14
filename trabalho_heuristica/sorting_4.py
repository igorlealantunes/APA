#
# Trabalho Ordenacao Heuristica
# 
# Aluno 	 : Igor Leal Antunes
# Matr  	 : 11211416
# Disciplina : Analise e Projeto de Algoritmos - 2016.2
# Professor  : Leonardo Cesar Teonacio Bezerra
#

#https://www.filosophy.org/post/32/python_function_execution_deadlines__in_simple_examples/
# Essa classe lancara execoes caso o algoritimo tome mais que X segundos para acabar
max_execution_time = 300 # 300 segundos = 5 minutos

import signal
class TimedOutExc(Exception):
  pass

def deadline(timeout, *args):
  def decorate(f):
	def handler(signum, frame):
	  raise TimedOutExc()

	def new_f(*args):

	  signal.signal(signal.SIGALRM, handler)
	  signal.alarm(timeout)
	  return f(*args)
	  signa.alarm(0)

	new_f.__name__ = f.__name__
	return new_f
  return decorate

import sys
sys.setrecursionlimit(9999999)


####################################################
####################################################
####################################################
############# Inicio definicao de funcoes ##########
####################################################
####################################################
####################################################
 
@deadline(max_execution_time)
def selection_sort(unsorted_array) :

	# copia a lista para nao mudar os valores da lista original
	clone = unsorted_array[:]

	for i in range(len(clone)) :
		
		# segura a posicao do menor valor
		smallest_pointer = i

		# varre a lista a partir da posicao i 
		# para nao desordenar o que ja esta ordenado
		for j in range(i, len(clone)):

			if clone[j] < clone[smallest_pointer]:
				smallest_pointer = j
			
		aux = clone[i]
		clone[i] = clone[smallest_pointer]
		clone[smallest_pointer] = aux

	return clone


#print selection_sort(array)

@deadline(max_execution_time)
def insertion_sort(unsorted_array):

	clone = unsorted_array[:]

	# varre a lista
	for i in range(len(clone)):

		value = clone[i]
		pos   = i 

		# pos > 0 			   => ter certeza que nao vai voltar mais do que o necessario
		# clone[pos-1] > value => ir voltando ate que a sublista estiver ordenada 
		while pos > 0 and clone[pos-1] > value:
			clone[pos] = clone[pos-1]
			pos = pos - 1

		# insere o elemento na posicao correta
		clone[pos] = value

	return clone

#print insertion_sort(array)

# usado no merge sort => NAO DEVE SER CHAMADO
def _merge(a,b):

	# array auxiliar
	c = []

	#realiza o `sorting` real nas partes do array ( esquerda e direita )
	while len(a) != 0 and len(b) != 0:

		# adiciona das partes A ou B para array C do menor para o maior
		if a[0] < b[0]:
			c.append(a[0])
			a.remove(a[0]) # importante quando copiar o restante para C
		else:
			c.append(b[0])
			b.remove(b[0]) # importante quando copiar o restante para C

	# copia o restante para C
	if len(a) == 0:
		c += b
	else:
		c += a
	return c

#usado para recursao (NAO DEVE SER CHAMADO DIRETAMENTE)
def _merge_sort(unsorted_array):

	# para recursao se o valor da lista for < 1 ( 0 para casos impares )
	if len(unsorted_array) == 0 or len(unsorted_array) == 1 :
		return unsorted_array
	else : # divide lista em dois e chama recursao de novo
		middle = len(unsorted_array)/2
		a = _merge_sort(unsorted_array[:middle])
		b = _merge_sort(unsorted_array[middle:])
		return _merge(a,b) # finalmente junta as partes para formar a lista ordenada

#usado para chamar a funcao recursiva e nao alterar o array original
@deadline(max_execution_time)
def merge_sort(unsorted_array):
	clone = unsorted_array[:]
	return _merge_sort(clone)

#print merge_sort(array)  



#  Primeiro transformamos a lista num heap ( arvore binaria, onde o pai eh sempre > que os filhos )
@deadline(max_execution_time)
def heap_sort( unsorted_array ):

	clone = unsorted_array[:]

	# Transforma num heap
	length = len( clone ) - 1
	leastParent = length / 2
	for i in range ( leastParent, -1, -1 ):
		_fix_heap( clone, i, length )

	# ordena o array (retirando o maior valor do heap)
	# Em seguida reorganiza o heap
	for i in range ( length, 0, -1 ):
		if clone[0] > clone[i]: 
			# troca elementos
			temp = clone[0];
			clone[0] = clone[i]
			clone[i] = temp

			# reagrupa o heap
			_fix_heap( clone, 0, i - 1 ) # reorganiza o heap
	
	return clone

#  Essa funcao checa se a lista eh um heap
#  
#  Filho direito  => 2n+2
#  Filgo esquerdo => 2n+1
#  
def _fix_heap( my_list, first, last ):

	# inicia o maior como filho esquerdo (tanto faz agora)
	largest = 2 * first + 1
	while largest <= last:
		# `largest` faz parte do array e eh maior que o filho esquero
		if ( largest < last ) and ( my_list[largest] < my_list[largest + 1] ):
			largest += 1

		# checa se o maior filho eh maior que o pai
		if my_list[largest] > my_list[first]:
			# troca elementos
			temp = my_list[largest];
			my_list[largest] = my_list[first]
			my_list[first] = temp
			
			# move para o maior filho nesse no
			first = largest;

			# volta ponteiro 
			largest = 2 * first + 1
		else:
			return


# print heap_sort(array)

@deadline(max_execution_time)
def quick_sort(unsorted_array):
	clone = unsorted_array[:]
	_quick_sort(clone, 0, len(clone)-1)
	return clone

def _quick_sort(my_list,first,last):

	if first < last:

		splitpoint = _partition(my_list,first,last)

		_quick_sort(my_list,first,splitpoint-1)
		_quick_sort(my_list,splitpoint+1,last)


def _partition(alist,first,last):

	# simplesmente escolhe se o valor do pivot como primeiro elemento
	pivotvalue = alist[first]

	# inicia ponteiro esquero uma posicao a mais do pivot
	leftmark = first+1
	# ponteiro `direito` sera posto no ultimo elemento
	rightmark = last

	# controla a execucao do script
	done = False
	while not done:
		# enquanto os ponteiros `esquerdo` e `direito` nao se cruzam
		# e o `esquero` <= pivot => anda pra direita 
		# 
		# (vai parar quando os ponteiros se cruzam ou quando 
		#  o valor do pivot <= do ponteiro )
		while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
			leftmark = leftmark + 1

		# enquanto os ponteiros `esquerdo` e `direito` nao se cruzam
		# e o `direito` >= pivot => anda pra esquerda
		while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark = rightmark -1

		# checa se os ponteiros se cruzaram
		# se sim => nada para trocar
		if rightmark < leftmark:
			done = True
		else: # trocam os valores dos ponteiros `esquerdo` e `direito`
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp

	# troca o valor do primeiro el com o do ponteiro `direito`
	temp = alist[first]
	alist[first] = alist[rightmark]
	alist[rightmark] = temp

	#retorna o novo valor do pivot
	return rightmark





def counting_sort(unsorted_array):

	clone = unsorted_array[:]
	# assume o tamanho do array baseado no maior valor inteiro
	num_positions = max(clone) 

	# balde para segurar os elements em chave => valores
	bucket = [0] * ( num_positions + 1 )
	for i in clone:
		bucket[i] += 1 # conta os elementos e armazena no indice = seu valor

	pos_atual = 0; # contador
	#varre o balde e distribui os valores no array
	for i in range( len( bucket ) ):
		while 0 < bucket[i]: # esvazia ate o ultimo elemento
			clone[pos_atual] = i # atribui valor no array ja ordenado
			pos_atual += 1 #incrementa contador do array final
			bucket[i] -= 1 #decrementa contador do balde
		

	return clone

# auxiliar para o bucket sort
def _insertion_sort(unsorted_array):
	# varre a lista
	for i in range(len(unsorted_array)):

		value = unsorted_array[i]
		pos   = i 

		# pos > 0 			   => ter certeza que nao vai voltar mais do que o necessario
		# unsorted_array[pos-1] > value => ir voltando ate que a sublista estiver ordenada 
		while pos > 0 and unsorted_array[pos-1] > value:
			unsorted_array[pos] = unsorted_array[pos-1]
			pos = pos - 1

		# insere o elemento na posicao correta
		unsorted_array[pos] = value

def bucket_sort(unsorted_array):
	
	import math

	clone = unsorted_array[:]

	if len(clone) == 0:
		return clone

	# estima se o melhor tamanho do bucket
	bucket_size = math.sqrt(len(clone))
	# Determine minimum and maximum values

	min_value = min(clone)
	max_value = max(clone)

	num_buckets = int(math.floor((max_value - min_value) / bucket_size) + 1)

	# inicia lista de buckets
	buckets = [ [] for i in range(num_buckets) ]

	#inicia os buckets com seus respectivos elementos
	for i in range(len(clone)):
		buckets[int(math.floor((clone[i] - min_value) / bucket_size))].append(clone[i])

	
	clone = []
	#para cada bucket => aplica insertion sort e cola array ordenado no resultado
	for i in range(len(buckets)):
		_insertion_sort(buckets[i])

		for j in range(len(buckets[i])):
			clone.append(buckets[i][j])

	return clone


def radix_sort(unsorted_array):

	clone = unsorted_array[:]

	# acha maior valor 
	max_number = max(clone)

	# assume numero de bins baseado no tamanho do maior valor
	num_bins = len(str(max_number))

	# cria os bins e armazena no array
	bins = [ [] for _ in range(num_bins) ]

	r = 1
	while max_number > r:
		
		# atribui cada numero ao seu bin ( de acordo com a quantidade de digitos )
		for e in clone:
			index = ( e / r ) % num_bins
			bins[index].append(e)

		r = r * num_bins

		# junta os bins, formando a lista ordenada
		clone = []
		for i in range(num_bins):
			clone.extend(bins[i])
			bins[i] = []

	return clone

####################################################
####################################################
####################################################
############# Fim definicao de funcoes #############
####################################################
####################################################
####################################################
 
def choose_best_func(unsorted_array):

	#checar se eh possivel usar algr lineares
	if _is_linear(unsorted_array) :
		if len(unsorted_array) < 100000:
			return bucket_sort
		else:
			return radix_sort
			
	else: # algoritmos tradicionais
		
		OD = _ordination_degree(unsorted_array)
		print OD

		if len(unsorted_array) < 30 and OD > 70 :
			return insertion_sort
		elif OD > 70:
			return heap_sort
		else:
			return quick_sort
		


def _is_linear(unsorted_array):
	# checa se eh inteiro >= 0
	return all( (isinstance(i, int) and i >= 0 ) for i in unsorted_array )

# calcula o grau de ordenacao, simplesmente comparando o numero com o seu sucessor
# e realizando uma estatistica
def _ordination_degree(unsorted_array):
	num_correct_pos = 0
	for i in range(0, len(unsorted_array) - 1):
		if(unsorted_array[i] < unsorted_array[i+1]):
			num_correct_pos = num_correct_pos + 1

	return (num_correct_pos / (len(unsorted_array) + 0.0)) * 100


# TODO 
def _find_num_buckets(unsorted_array):
	import math
	bucket_size = math.sqrt(len(unsorted_array))

	min_value = min(unsorted_array)
	max_value = max(unsorted_array)

	num_buckets = int(math.floor((max_value - min_value) / bucket_size) + 1)

	# inicia lista de buckets
	buckets = [ [] for i in range(num_buckets) ]

	#inicia os buckets com seus respectivos elementos
	for i in range(len(unsorted_array)):
		buckets[int(math.floor((unsorted_array[i] - min_value) / bucket_size))].append(unsorted_array[i])

	empty_bukets = 0
	for x in buckets:
		print len(x)
		if( len(x) == 0):
			empty_bukets = empty_bukets + 1

	print empty_bukets

import os
import time


function_to_call = ""
unsorted_array = []

# le numero de entradas
num_entradas = input()

print "Reading input..."
# transforma em uma lista de inteiros
for x in range(num_entradas):

	try:
		input_val = input()
		i = int(input_val)
		unsorted_array.append(i)
	except ValueError:
		pass

print "Read input !"
# Choose best function to call
function_to_call = choose_best_func(unsorted_array)

start_time = time.time()
bucket_sort(unsorted_array)
end = time.time()
time_taken = (time.time() - start_time)
print("\t Bucket --- %s seconds ---" % time_taken)

start_time = time.time()
radix_sort(unsorted_array)
end = time.time()
time_taken = (time.time() - start_time)
print("\t Radix --- %s seconds ---" % time_taken)



print "Using " + function_to_call.__name__


#_find_num_buckets(unsorted_array)

# roda o algoritmo
#sorted_array = function_to_call(unsorted_array)

#imprime na stdout
#for x in sorted_array:
#	print x














