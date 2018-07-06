"""
Método dos Mínimos Quadrados

Desenvolvido por:
	- Karine Pestana
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

#python3 MMQ.py -l 5 -c 2 -f 1 -v 0.30 2.75 4.50 5.95 7.80 1.80 1.90 3.10 3.90 3.30
#python3 MMQ.py -l 10 -c 2 -f 1 -v 1 2 3 4 5 6 7 8 9 10 1.3 3.5 4.2 5 7 8.8 10.1 12.5 13 15.6
#python3 MMQ.py -l 4 -c 2 -f 1 -v 1 2 3 4 3 5 6 8

import argparse
import matplotlib.pyplot as plt
import numpy as np

# Leitura dos argumentos por linha de comando
ap = argparse.ArgumentParser()
ap.add_argument('-l', "--l", required=True, help="Numero de linhas da matriz")
ap.add_argument('-c', "--c", required=True, help="Numero de colunas da matriz")
ap.add_argument('-f', "--f", required=True, help="Funções: 1-reta; 2-curva; 3-polinimio")
ap.add_argument('-v', "--v", required=True, nargs='+', help="Valores da matriz")

args = vars(ap.parse_args())
n = int((int(args["l"]) * int(args["c"]))/2)
funcao = args["f"]
valores = list(map(float, args["v"]))

#Implementação da reta

if (funcao == "1"):
	x = np.array(valores[:int(len(valores)/2)])
	y = np.array(valores[int(len(valores)/2):])

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
#	print(a0, a1)

	result = a0 + a1*x
#	print(result)

	plt.plot( x, y, 'go', x, result, "-b") # linha azul com bolinhas verdes
	plt.title("Reta com o mínimo erro")
	plt.grid(True)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show()
