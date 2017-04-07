
#
# Trabalho Mochila
# 
# Aluno 	 : Igor Leal Antunes (11211416) e Fernando Souza (11218354)
# Disciplina : Analise e Projeto de Algoritmos - 2016.2
# Professor  : GILBERTO FARIAS DE SOUSA FILHO 
#
#
# uso : 
# 		utilizando pipe de arquivo:
# 			> python mochila.py < nome_do_arquivo
# 
# 		ou
#		
#		Digitando a entrada direto no console
#		
#			> python mochila.py
#			> 7 23
#			> 1 2 5 6 7 9 11
#			> 1 6 18 22 28 40 60
#		
#					

n, total_w = [ int(_) for _ in raw_input().split() ]


# guarda pesos
w_list = [0] + [ int(num) for num in raw_input().split() ]

# guarda os valores
v_list = [0] + [ int(num) for num in raw_input().split() ]

x = total_w + 1
y = len(w_list)

# cria matrix 
matrix = [ [0 for i in range(x)] for j in range(y)]

# guarda 1 se usar e 0 se nao usar
usage_matrix = [ [0 for i in range(x)] for j in range(y)]


for i in xrange(1, y):
	for j in xrange(1, x):
		indice_objeto = i # coluna
		peso_disponivel = j # linha

		peso_obj  = w_list[indice_objeto]
		valor_obj = v_list[indice_objeto]

		#print "Peso: " + str(peso_obj) + "valor: " + str(valor_obj) + " avaliando peso: " + str(peso_disponivel)
		
		if peso_obj > peso_disponivel :
			#print "peso maior... utilizando de cima ( " + str(matrix[i - 1][j])+" )"
			valorij = matrix[i - 1][j] # valor de cima
			usage_matrix[i][j] = 0
		else:
			#print "peso menor ou igual"

			max_obj_atual = valor_obj
			peso_disponivel_restante = peso_disponivel - peso_obj

			#print "peso disponivel " + str(peso_disponivel_restante)
			#print "possivel adicao " + str(matrix[i - 1][peso_disponivel_restante])
			max_obj_atual = max_obj_atual + matrix[i - 1][peso_disponivel_restante]

			#print "peso de cima" + str(matrix[i - 1][j])
			# se o max do obj atual for > do que o de cima
			if(max_obj_atual > matrix[i - 1][j]):
				valorij = max_obj_atual
				usage_matrix[i][j] = 1
			else: # se nao, usa o peso de cima
				valorij = matrix[i - 1][j]
				usage_matrix[i][j] = 0

		
		matrix[i][j] = valorij
		#print '\n'.join([' '.join(str(row)) for row in matrix])


# calculando a melhor combinacao para peso maximo	
	
I = len(w_list) - 1 # item atual
W = total_w         # peso restante 

items_usados = []
valor_final = matrix[I][W]

while I > 0 and W > 0:
	el = usage_matrix[I][W]
	peso_obj  = w_list[I]

	#print "Item " + str(I) + " Coluna " + str(W) + " Peso Obj: " + str(peso_obj)

	if el == 0:
		I = I - 1
	else:
		items_usados.append(I)
		I = I - 1
		W = W - peso_obj

	#print " Peso restante " + str(W)


print ""
print "Items usados : "
print items_usados

print "Valor Final da mochila : " + str(valor_final)
	
