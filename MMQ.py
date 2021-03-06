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
	-g: Grau 
		O Grau deve ser fornecido se a função for polinomial, informando qual é o grau do polinomio que se deseja ajustar a função
"""

#Testes para a função 1
#python3 MMQ.py -l 5 -c 2 -f 1 -v 0.30 2.75 4.50 5.95 7.80 1.80 1.90 3.10 3.90 3.30
#python3 MMQ.py -l 10 -c 2 -f 1 -v 1 2 3 4 5 6 7 8 9 10 1.3 3.5 4.2 5 7 8.8 10.1 12.5 13 15.6
#python3 MMQ.py -l 4 -c 2 -f 1 -v 1 2 3 4 3 5 6 8

#Testes para a função 2
#python3 MMQ.py -l 4 -c 1 -f 2 -v -1.5 -0.5 1.25 1.5 1.15 -0.37 0.17 0.94
#python3 MMQ.py -l 8 -c 2 -f 2 -v -1 0 1 2 4 5 5 6 -2 -1 0 1 1 2 3 4 13 11 9 4 11 9 1 -1

#Testes para a função 3
#python3 MMQ.py -l 6 -c 2 -f 3 -g 2 -v -2.0 -1.5 0.0 1.0 2.2 3.1 -30.5 -20.2 -3.3 8.9 16.8 21.4

import argparse
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.linalg import lu_factor, lu_solve

# Leitura dos argumentos por linha de comando
ap = argparse.ArgumentParser()
ap.add_argument('-l', "--l", required=True, help="Numero de linhas da matriz")
ap.add_argument('-c', "--c", required=True, help="Numero de colunas da matriz")
ap.add_argument('-f', "--f", required=True, help="Funções: 1-reta; 2-curva; 3-polinimio")
ap.add_argument('-v', "--v", required=True, nargs='+', help="Valores da matriz")
ap.add_argument('-g', "--g", required=False, help="Grau do polinômio que se deseja ajustar a função")

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
	sum_x = round(sum(x),2)
	sum_y = round(sum(y),2)
	sum_x_quad = round(sum(x_quad), 2)
	sum_y_quad = round(sum(y_quad),2)
	sum_x_y = round(sum(x_y),2)
	#print(sum_x, sum_y, sum_x_y, sum_x_quad)
	
	a0 = round(abs((sum_x_y * sum_x - sum_y * sum_x_quad)/(n* sum_x_quad - ((sum_x)*(sum_x)))), 2) #Aplicacao formula para a0
	a1 = round((n * sum_x_y - sum_x * sum_y)/ (n*sum_x_quad - ((sum_x)*(sum_x))), 2) #Aplicacao formula para a1
	print(a0, a1)

	result = a0 + a1*x
	print(result)

	plt.plot( x, y, 'bo', x, result, "-b") 
	plt.title("Ajuste Linear simples com o mínimo erro")
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
			#print(i,j, x[j-1], x[i-1])
				
	somatorio = np.zeros(shape=[num_eq,1]) 
	somatorio[0] = sum(y)
	for i in range(0, num_eq-1):
		somatorio[i+1] = sum(x[i]*y) 

	coeficientes = lu_solve(lu_factor(matrix_X), somatorio) #resolve sistema linear por LU

	print("X: \n", x)
	print("Y: \n", y)
	print("Matriz X: \n", matrix_X)
	print("Somatorio: \n", somatorio)
	print("Coeficientes: \n", coeficientes) #primeiro coeficiente é termo independente e demais são x1, x2... xn

	#result = coeficientes[0] + coeficientes[1] * x[0] + coeficientes[2] * x[1] 
	
	result = 0
	for i in range(0, num_eq):
		if (i == 0):
			result += coeficientes[0][0]
		else:
			result += coeficientes[i][0] * x[i-1]
	
	print(result)

	colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
	for i in range(0, num_eq-1):
		plt.plot( x[i], y, colors[i] + 'o', x[i], result, "-" + colors[i])
	
	plt.title("Ajuste linear múltiplo com o mínimo erro")
	plt.grid(True)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show()
	
elif (funcao == "3"):
	#Pega o grau do polinomio que se deseja ajustar
	grau = int(args["g"])
	
	#X e Y vindos da linha de comando
	x = np.array(valores[:int(len(valores)/2)])
	y = np.array(valores[int(len(valores)/2):])

	#Cria matriz X quadrada com 0 do tamanho de grau+1
	matrix_X = np.zeros(shape=[grau+1, grau+1]) 

	matrix_X[0][0] = n
	for i in range(0, matrix_X.shape[0]):
		for j in range(1, matrix_X.shape[1]):
			#primeira linha
			matrix_X[i][j] = round(sum(pow(x, j+i)), 2)
			matrix_X[j][i] = round(sum(pow(x, j+i)), 2)	
	
	somatorio = np.zeros(shape=[grau+1,1]) 
	somatorio[0] = sum(y)
	
	for i in range(1, grau+1):
		somatorio[i] = round(sum(pow(x, i)*y), 2)

	coeficientes = lu_solve(lu_factor(matrix_X), somatorio) #resolve sistema linear por LU

	print("X: \n", x)
	print("Y: \n", y)
	print("Matriz X: \n", matrix_X)
	print("Somatorio: \n", somatorio)
	print("Coeficientes: \n", coeficientes) #primeiro coeficiente é termo independente e demais são x1, x2... xn

	result = 0
	i = 0
	for i in range(0, grau+1):
		print(i)
		result += coeficientes[i]*pow(x, i)

	print(result)

	plt.plot( x, y, 'go', x, result, "-g")
	plt.title("Ajuste linear polinomial com o mínimo erro")
	plt.grid(True)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show()
	
