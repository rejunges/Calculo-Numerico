"""
Derivação por formulas de diferenças divididas

Desenvolvido por:
	- Karine Pestana
	- Marcelo Bonoto
	- Renata Junges

Disciplina: 
	Cálculo Numérico Computacional 2018-1

Argumentos:
	-x: 
	-h: 
	-f(x): função 
"""

#python3 Derivacao.py -x 0.5 -H 0.5 -f 2/x-4

import argparse
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.linalg import lu_factor, lu_solve

# Leitura dos argumentos por linha de comando
ap = argparse.ArgumentParser()
ap.add_argument('-x', "--x", required=True, help="Entrada x")
ap.add_argument('-H', "--h", required=True, help="Entrada h")
ap.add_argument('-f', "--f", required=True, help="Funcao")

args = vars(ap.parse_args())
x = args["x"]
h = float(args["h"])
f = args["f"]

print("\n ---------------------------- Entradas ----------------------------\n")
print("X: ", x)
print("H: ", h)
print("F: ", f)

#assumo que fx contém os valores da função desde fx(x-5), fx(x-4), fx(x-3), fx(x-2), fx(x-1) até fx(x+5)
fx = np.array([1, 2, 20, 4, 5, 50, 30, 8, 9, 10, 11])
tam = len(fx)//2

#crio as listas para armazenar as derivadas
progressiva = []
regressiva = []
centrada = []

def dev_progressiva(fx):
	#primeira derivada
	progressiva.append(float(fx[tam+1] + fx[tam])/h)

	#segunda derivada
	progressiva.append(float(fx[tam+2]-2*fx[tam+1]+fx[tam])/pow(h,2))

	#terceira derivada
	progressiva.append(float(fx[tam+3] - 3*fx[tam+2] + 3*fx[tam+1] - fx[tam])/pow(h,3))

	#quarta derivada
	progressiva.append(float(fx[tam+4] - 4*fx[tam+3] + 6*fx[tam+2] - 4*fx[tam+1] + fx[tam])/pow(h,4))

	i = 0
	print("\n---------------------------- Derivada Progressiva ----------------------------\n")
	for i in range(0, len(progressiva)):
		print(i+1,"º derivada:", progressiva[i])

def dev_regressiva(fx):
	#primeira derivada
	regressiva.append(float(fx[tam] - fx[tam-1])/h)

	#segunda derivada
	regressiva.append(float(fx[tam]-2*fx[tam-1]+fx[tam-2])/pow(h,2))

	#terceira derivada
	regressiva.append(float(fx[tam] - 3*fx[tam-1] + 3*fx[tam-2] - fx[tam-3])/pow(h,3))

	#quarta derivada
	regressiva.append(float(fx[tam] - 4*fx[tam-1] + 6*fx[tam-2] - 4*fx[tam-3] + fx[tam-4])/pow(h,4))

	i = 0
	print("\n---------------------------- Derivada Regressiva ----------------------------\n")
	for i in range(0, len(regressiva)):
		print(i+1,"º derivada:", regressiva[i])

def dev_centrada(fx):
	#primeira derivada
	centrada.append(float(fx[tam+1] - fx[tam-1])/2*h)

	#segunda derivada
	centrada.append(float(fx[tam+1]-2*fx[tam]+fx[tam-1])/pow(h,2))

	#terceira derivada
	centrada.append(float(fx[tam+2] - 2*fx[tam+1] + 2*fx[tam-1] - fx[tam-2])/(2*pow(h,3)))

	#quarta derivada
	centrada.append(float(fx[tam+2] - 4*fx[tam+1] + 6*fx[tam] - 4*fx[tam-1] + fx[tam-2])/pow(h,4))

	i = 0
	print("\n----------------------------- Derivada Centrada -----------------------------\n")
	for i in range(0, len(centrada)):
		print(i+1,"º derivada:", centrada[i])

dev_progressiva(fx)
dev_regressiva(fx)
dev_centrada(fx)