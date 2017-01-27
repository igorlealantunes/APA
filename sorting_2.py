#
# Trabalho Ordenacao 02
# 
# Aluno 	 : Igor Leal Antunes
# Matr  	 : 11211416
# Disciplina : Analise e Projeto de Algoritmos - 2016.2
# Professor  : Leonardo Cesar Teonacio Bezerra
#




####################################################
####################################################
####################################################
############# Inicio definicao de funcoes ##########
####################################################
####################################################
####################################################
 

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
def merge_sort(unsorted_array):
	clone = unsorted_array[:]
	return _merge_sort(clone)

#print merge_sort(array)  



#  Primeiro transformamos a lista num heap ( arvore binaria, onde o pai eh sempre > que os filhos )
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

####################################################
####################################################
####################################################
############# Fim definicao de funcoes #############
####################################################
####################################################
####################################################
 

import os
import time

path = './instancias'

inputs = {"10" : [], "50" : [], "90" : []}

sorting_functions = [ selection_sort, insertion_sort, merge_sort, heap_sort, quick_sort ]

for filename in os.listdir(path):
	category = filename.split(".")[0]

	inputs[category].append(filename)


for input_type in inputs:
	for file in inputs[input_type]:
		
		full_path = path + "/" + file
		with open(full_path) as f:
			content = f.readlines()

			### This will take most time to execute ( the files are very large )
    		integers = map(int, content)[1:] # delete first element (number of numbers in the file)

    		#print (integers[:100])

    		for func in sorting_functions:
    			start_time = time.time()
	    		print "Executing " + func.__name__ + " In " + file
	    		func(integers[:100])
	    		end = time.time()
	    		print("--- %s seconds ---" % (time.time() - start_time))
    		






















