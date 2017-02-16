#
# Trabalho Ordenacao Heuristica
# 
# Aluno 	 : Igor Leal Antunes (11211416) && Fernando Souza (11218354)
# Disciplina : Analise e Projeto de Algoritmos - 2016.2
# Professor  : Leonardo Cesar Teonacio Bezerra
#

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

@deadline(max_execution_time)
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

@deadline(max_execution_time)
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

@deadline(max_execution_time)
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

@deadline(max_execution_time)
def radix_sort_string(unsorted_array, pos = 0):

	clone = unsorted_array[:]

	if len(clone) <= 1:
		return clone

	done_bucket = []
	
	# 27 => numero de letras no alfabeto
	buckets = [ [] for x in range(27) ] 

	for s in clone:
		# se ja checou ao final da string
		if pos >= len(s):
			done_bucket.append(s)
		else: # se nao continua inserindo
			buckets[ord(s[pos]) - ord('a') ].append(s)

	# chama o radix pra string no proximo bucket recusivamente
	buckets = [ radix_sort_string(b, pos + 1) for b in buckets ]

	return done_bucket + [ b for blist in buckets for b in blist ]

####################################################
####################################################
####################################################
############# Fim definicao de funcoes #############
####################################################
####################################################
####################################################
 
# Vai retornar o melhor algoritmo de acordo com nossa heuristica
def choose_best_func(unsorted_array):

	is_string = _is_string(unsorted_array)

	# se entrada for string utilizar radix sort
	if(is_string):
		return radix_sort_string

	#checar se eh possivel usar algr lineares
	if _is_linear_good(unsorted_array) :

		max_value = max(unsorted_array)
		
		# se o maximo valor for pequeno => counting sort ira utilizar menos memoria
		if max_value < 1000000: 
			return counting_sort
		else:
			return radix_sort
			
	else: # algoritmos tradicionais
		return quick_sort
		
#checa se valores sao strings
def _is_string(unsorted_array):
	for i in range(0, len(unsorted_array)):
		if( not isinstance(unsorted_array[i], str) ):
			return False

	return True

# checa se seria bom utilizar algoritmos lineares
def _is_linear_good(unsorted_array):

	max_value = max(unsorted_array)

	# se o numero tiver muitas casas deciamis => melhor utilizar algr tradicionais
	if( len(str(max_value)) > 8):
		return False

	for i in range(0, len(unsorted_array)):
		if( (not isinstance(unsorted_array[i], int)) or unsorted_array[i] < 0):
			return False

	return True

# calcula o grau de ordenacao, simplesmente comparando o numero com o seu sucessor
# e realizando um calculo estatistico
"""def _ordination_degree(unsorted_array):
	num_correct_pos = 0
	for i in range(0, len(unsorted_array) - 1):
		if(unsorted_array[i] < unsorted_array[i+1]):
			num_correct_pos = num_correct_pos + 1

	return (num_correct_pos / (len(unsorted_array) + 0.0)) * 100"""

# transforma a entrada para casos onde exista numeros negativos
def _treat_input(unsorted_array):

	min_value = min(unsorted_array)
	if(min_value < 0):
		for i in range(0, len(unsorted_array)):
			unsorted_array[i] = unsorted_array[i] + (- min_value)

	return min_value

import os
import time


function_to_call = ""
unsorted_array = []


# pega a pasta para ler como primeiro parametro
path = sys.argv[1]


from pprint import pprint

num_files = 0
inputs = []

for filename in os.listdir(path):
	num_files = num_files + 1

	try:
		inputs.append(filename)
		num_files = num_files + 1
	except KeyError:
		pass

counter = 0
for file in inputs:
		
	counter = counter + 1 
	print counter 
	full_path = path + "/" + file
	with open(full_path) as f:
		content = f.readlines()

		try:
			test_value = int(content[2])
			is_string = False
		except ValueError:
			is_string = True
			pass


		if not is_string:
			is_string = False
			input_array = map(int, content)[1:] # delete first element (number of numbers in the file)
		else:
			is_string = True
			input_array = map(str, content)[1:] # delete first element (number of numbers in the file)

		start_time = time.time()
		

		#Tratando a entrada (transformando array todo em positivos) =>
		if( not is_string):
			min_value = _treat_input(input_array)

		try:

			#print input_array
			function_to_call = choose_best_func(input_array)

			#print function_to_call
			#exit()

			print ""
			print "Executing " + function_to_call.__name__ + " In " + file
			
			sorted_array = function_to_call(input_array)

			# soma o valor minimo de volta no array se a entrada foi negativa
			if( not is_string):
				if(min_value < 0):
					for i in range(0, len(sorted_array)):
						sorted_array[i] = sorted_array[i] + min_value

		except TimedOutExc as e:
			print "\tMax Execution time reached"

		finally:	
			end = time.time()
			time_taken = (time.time() - start_time)
			print("\t--- %s seconds ---" % time_taken)














