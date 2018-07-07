"""
Método dos Mínimos Quadrados

Desenvolvido por:
	- Karine Pestana
	- Marcelo Bonoto
	- Renata Junges

Disciplina: 
	Cálculo Numérico Computacional 2018-1

Argumentos:
	-l: Linhas
	-c: Colunas
	-f: Função
		1 para reta
		2 para curva
		3 para polinomio
	-v: Valores
"""

#Testes para a funções de reta
#python3 MMQ.py -l 5 -c 2 -f 1 -v 0.30 2.75 4.50 5.95 7.80 1.80 1.90 3.10 3.90 3.30
#python3 MMQ.py -l 10 -c 2 -f 1 -v 1 2 3 4 5 6 7 8 9 10 1.3 3.5 4.2 5 7 8.8 10.1 12.5 13 15.6
#python3 MMQ.py -l 4 -c 2 -f 1 -v 1 2 3 4 3 5 6 8

#python3 MMQ.py -l 12 -c 2 -f 2 -v 100 90 80 70 70 70 70 65 60 60 55 50 550 630 720 700 625 735 560 715 750 690 715 650 55 70 90 100 90 105 80 110 125 115 130 130
#python3 MMQ.py -l 4 -c 2 -f 2 -v 1 2 3 4 3 5 6 8


import argparse
import matplotlib.pyplot as plt
import numpy as np
import math

def symmetrize(a):
    return a + a.T - np.diag(a.diagonal())

# Leitura dos argumentos por linha de comando
ap = argparse.ArgumentParser()
ap.add_argument('-l', "--l", required=True, help="Numero de linhas da matriz")
ap.add_argument('-c', "--c", required=True, help="Numero de colunas da matriz")
ap.add_argument('-f', "--f", required=True, help="Funções: 1-reta; 2-curva; 3-polinimio")
ap.add_argument('-v', "--v", required=True, nargs='+', help="Valores da matriz")

args = vars(ap.parse_args())
n = int(args["l"])
funcao = args["f"]
valores = list(map(float, args["v"]))

if (funcao == "1"):
	x = np.array(valores[:int(len(valores)/2)])
	y = np.array(valores[int(len(valores)/2):])
	#Implementação da reta
	x_quad = x*x
	y_quad = y*y
	x_y = x*y
	sum_x = sum(x)
	sum_y = sum(y)
	sum_x_quad = sum(x_quad)
	sum_y_quad = sum(y_quad)
	sum_x_y = sum(x_y)

	a0 = round(abs((sum_x_y * sum_x - sum_y * sum_x_quad)/(n* sum_x_quad - ((sum_x)*(sum_x)))), 2) #Aplicacao formula para a0
	a1 = round((n * sum_x_y - sum_x * sum_y)/ (n*sum_x_quad - ((sum_x)*(sum_x))), 2) #Aplicacao formula para a1
	print(a0, a1)

	result = a0 + a1*x
	print(result)

	plt.plot( x, y, 'go', x, result, "-b") # linha azul com bolinhas verdes
	plt.title("Reta com o mínimo erro")
	plt.grid(True)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show()

elif (funcao == "2"):
	#Implementacao da curva
	num_eq = int(args["c"]) + 1 #numero total de equações (número de colunas + 1)
	
	#x contem o valor dos x (x = numero de equações-1)
	x = np.zeros(shape=[int(args["c"]), int(args["l"])])
	k = 0

	for i in range(x.shape[0]):
		for j in range(x.shape[1]):
			x[i][j] = valores[k]
			k = k + 1
	#y são os ultimos valores de valores
	y = np.zeros(shape=[1, int(args["l"])])
	y = valores[k:len(valores)]

	

	matrix_X = np.zeros(shape=[num_eq, num_eq]) 

	#Cria primeira linha e primeira coluna	
	matrix_X[0][0] = n
	for j in range(1, matrix_X.shape[1]):
		#primeira linha
		matrix_X[0][j] = round(sum(x[j-1]), 2)
		matrix_X[j][0] = round(sum(x[j-1]), 2)
		
	#Coloca valor nas outras colunas
	for i in range(1, matrix_X.shape[0]):
		for j in range(1, matrix_X.shape[1]):
			matrix_X[i][j] = round(sum(x[i-1] * x[j-1]),2)
			print(i,j, x[j-1], x[i-1])
				
	somatorio = np.zeros(shape=[num_eq,1]) 
	somatorio[0] = sum(y)
	#for i in range(0, num_eq-1):
	#	somatorio[i+1] = sum(x[i]*y) 
	#matrix_X = np.matrix(matrix_X) #Faz isso pq se quiser a inversa precisa ser matriz não array
	
	#http://homepages.dcc.ufmg.br/~jussara/metq/aula6-2017-1-parte2.pdf -> ONDE TEM A FORMULA
	#b = (xTransposta * x)^Inversa * xTransposta*y

	print("X: \n", x)
	print("Y: \n", y)
	print("Matriz X: \n", matrix_X)
	print("Somatorio: \n", somatorio)
	

	#Testando uma alternativa
	n = int(args["l"])

	x = np.array(valores[:int(len(valores)/2)])
	y = np.array(valores[int(len(valores)/2):])
	
	y_ln = np.log(np.asarray(y))

	x_ln = np.log(np.asarray(x))


	#Implementação da reta
	x_quad = x*x
	y_quad = y*y
	x_y = x*y_ln
	sum_x = sum(x)
	sum_y = sum(y)
	sum_x_ln = sum(x_ln)
	sum_y_ln = sum(y_ln)
	sum_x_quad = sum(x_quad)
	sum_y_quad = sum(y_quad)
	sum_x_y = sum(x_y)

	a0 = abs((n*sum_x_y-sum_x*sum_y_ln)/(n*sum_x_quad-((sum_x)*(sum_x))))
	a1 = (sum_x*sum_x_y-sum_y_ln*sum_x_quad)/(((sum_x)*(sum_x))-n*sum_x_quad)
	
	#a0 = round(abs((sum_x_y * sum_x - sum_y * sum_x_quad)/(n* sum_x_quad - ((sum_x)*(sum_x)))), 2) #Aplicacao formula para a0
	#a1 = round((n * sum_x_y - sum_x * sum_y)/ (n*sum_x_quad - ((sum_x)*(sum_x))), 2) #Aplicacao formula para a1
	print(x)
	print(sum_x)
	print(y_ln)
	print(sum_y_ln)
	print(x_y)
	print(sum_x_y)
	print(x_quad)
	print(sum_x_quad)
	print(a0, a1)

	result = 2.37156* np.exp(a0*x)
	print(result)

	plt.plot( x, y, 'go', x, result, "-b") # linha azul com bolinhas verdes
	plt.title("Reta com o mínimo erro")
	plt.grid(True)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show()