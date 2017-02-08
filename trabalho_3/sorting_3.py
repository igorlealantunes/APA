#
# Trabalho Ordenacao 03
# 
# Aluno 	 : Igor Leal Antunes
# Matr  	 : 11211416
# Disciplina : Analise e Projeto de Algoritmos - 2016.2
# Professor  : Leonardo Cesar Teonacio Bezerra
#


import signal
import sys
import fileinput

sys.setrecursionlimit(9999999)


####################################################
####################################################
####################################################
############# Inicio definicao de funcoes ##########
####################################################
####################################################
####################################################
 
#@deadline(max_execution_time)
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
 


# primeiro parametro (typo da funcao)
sort_type = sys.argv[1]
function_to_call = ""
unsorted_array = []

# escolhe a funcao de acordo com o parametro entrado
if sort_type == "1" :	  
	function_to_call = counting_sort
elif sort_type == "2":
	function_to_call = bucket_sort
elif sort_type == "3":
	function_to_call = radix_sort
else:
	sys.exit("argv should be between 1 and 3")

# le numero de entradas
num_entradas = input()

# transforma em uma lista de inteiros
for x in range(num_entradas):

	try:
		input_val = input()
		i = int(input_val)
		unsorted_array.append(i)
	except ValueError:
		pass

# roda o algoritmo
sorted_array = function_to_call(unsorted_array)

#imprime na stdout
for x in sorted_array:
	print x

# fontes 

#http://www.growingwiththeweb.com/2015/06/bucket-sort.html
#https://www.quora.com/How-do-I-calculate-the-optimized-number-of-buckets-when-implementing-bucket-sort-followed-by-insertion-sort
#https://gist.github.com/rizkyabdilah/1740053
