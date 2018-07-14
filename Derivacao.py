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

print("---------------------------- Entradas ----------------------------\n")
print("X: ", x)
print("H: ", h)
print("F: ", f)

#assumo que fx contém os valores da função desde fx(x-5), fx(x-4), fx(x-3), fx(x-2), fx(x-1) até fx(x+5)
fx = np.array([1, 2, 3, 4, 5, 6, 30, 8, 9, 10, 11])
tam = len(fx)//2

progressiva = []

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
	print("---------------------------- Derivada Progressiva ----------------------------\n")
	for i in range(0, len(progressiva)):
		print("derivada", i+1, ": ", progressiva[i])


dev_progressiva(fx)
