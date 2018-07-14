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

#python3 Derivacao.py -x 0.5 -H 0.5 -f "(2/x-4)"
#python3 Derivacao.py -x 0.5 -H 0.25 -f "(-0.1*pow(x,4)-0.15*pow(x,3)-0.5*pow(x,2)-0.25*x+1.2)"
#python3 Derivacao.py -x 2 -H 0.25 -f "(pow(x,2)-1*2)"
#python3 Derivacao.py -x 1 -H 0.1 -f "(math.cos(x))"


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
x = float(args["x"])
h = float(args["h"])
f = args["f"]

#assumo que fx contém os valores da função desde fx(x-5) até fx(x+5)
fx = []

for i in range(-5, 6):
	fx.append(eval(f.replace("x", str(x+(i*h))))) #Faz o valor de x ocupar o "x" da função e faz com que essa string seja computada

print(fx)
print("\n ---------------------------- Entradas ----------------------------\n")
print("X: ", x)
print("H: ", h)
print("F: ", f)

tam = len(fx)//2

#crio as listas para armazenar as derivadas
progressiva = []
progressivaH2 = []
regressiva = []
regressivaH2 = []
centrada = []
centradaH2 = []

def dev_progressiva(fx):
	#primeira derivada
	progressiva.append(float(fx[tam+1] + fx[tam])/h)
	progressivaH2.append((-fx[tam+2] + 4*fx[tam+1] - 3*fx[tam])/(2*h))

	#segunda derivada
	progressiva.append(float(fx[tam+2]-2*fx[tam+1]+fx[tam])/pow(h,2))
	progressivaH2.append((-fx[tam+3] + 4*fx[tam+2] - 5*fx[tam+1] + 2*fx[tam])/pow(h,2))

	#terceira derivada
	progressiva.append(float(fx[tam+3] - 3*fx[tam+2] + 3*fx[tam+1] - fx[tam])/pow(h,3))
	progressivaH2.append((-3*fx[tam+4] + 14*fx[tam+3] - 24*fx[tam+2] + 18*fx[tam+1] - 5*fx[tam])/(2*pow(h,3)))

	#quarta derivada
	progressiva.append(float(fx[tam+4] - 4*fx[tam+3] + 6*fx[tam+2] - 4*fx[tam+1] + fx[tam])/pow(h,4))
	progressivaH2.append((-2*fx[tam+5] + 11*fx[tam+4] - 24*fx[tam+3] + 26*fx[tam+2] - 14*fx[tam+1] + 3*fx[tam])/pow(h, 4))

	print("\n---------------------------- Derivada Progressiva ----------------------------\n")
	for i in range(0, len(progressiva)):
		print(i+1,"º derivada O(h):", progressiva[i])
		print(i+1,"º derivada O(h²):", progressivaH2[i])
		print("\n")

def dev_regressiva(fx):
	#primeira derivada
	regressiva.append(float(fx[tam] - fx[tam-1])/h)
	regressivaH2.append((3*fx[tam] - 4*fx[tam-1] + fx[tam-2])/(2*h))

	#segunda derivada
	regressiva.append(float(fx[tam]-2*fx[tam-1]+fx[tam-2])/pow(h,2))
	regressivaH2.append((2*fx[tam] - 5*fx[tam-1] + 4*fx[tam-2] - fx[tam-3])/pow(h,2))

	#terceira derivada
	regressiva.append(float(fx[tam] - 3*fx[tam-1] + 3*fx[tam-2] - fx[tam-3])/pow(h,3))
	regressivaH2.append((5*fx[tam] - 18*fx[tam-1] + 24*fx[tam-2] - 14*fx[tam-3] + 3*fx[tam-4])/(2*pow(h,3)))
	
	#quarta derivada
	regressiva.append(float(fx[tam] - 4*fx[tam-1] + 6*fx[tam-2] - 4*fx[tam-3] + fx[tam-4])/pow(h,4))
	regressivaH2.append((3*fx[tam] - 14*fx[tam-1] + 26*fx[tam-2] - 24*fx[tam-3] + 11*fx[tam-4] - 2*fx[tam-5])/pow(h,4))
	
	print("---------------------------- Derivada Regressiva ----------------------------\n")
	for i in range(0, len(regressiva)):
		print(i+1,"º derivada O(h):", regressiva[i])
		print(i+1,"º derivada O(h²):", regressivaH2[i])
		print("\n")

def dev_centrada(fx):
	#primeira derivada
	centrada.append(float(fx[tam+1] - fx[tam-1])/2*h)
	centradaH2.append((-fx[tam+2] + 8*fx[tam+1] -8*fx[tam-1] + fx[tam-2])/(12*h))

	#segunda derivada
	centrada.append(float(fx[tam+1]-2*fx[tam]+fx[tam-1])/pow(h,2))
	centradaH2.append((-fx[tam+2] + 16*fx[tam+1] -30*fx[tam] + 16*fx[tam-1] - fx[tam-2])/(12*pow(h,2)))

	#terceira derivada
	centrada.append(float(fx[tam+2] - 2*fx[tam+1] + 2*fx[tam-1] - fx[tam-2])/(2*pow(h,3)))
	centradaH2.append((-fx[tam+3] + 8*fx[tam+2] - 13*fx[tam+1] + 13*fx[tam-1] - 8*fx[tam-2] + fx[tam-3])/(8*pow(h,3)))

	#quarta derivada
	centrada.append(float(fx[tam+2] - 4*fx[tam+1] + 6*fx[tam] - 4*fx[tam-1] + fx[tam-2])/pow(h,4))
	centradaH2.append((-fx[tam+3] + 12*fx[tam+2] - 39*fx[tam+1] + 56*fx[tam] - 39*fx[tam-1] + 12*fx[tam-2] - fx[tam-3])/(6*pow(h,4)))

	print("----------------------------- Derivada Centrada -----------------------------\n")
	for i in range(0, len(centrada)):
		print(i+1,"º derivada O(h²): ", centrada[i])
		print(i+1,"º derivada O(h^4): ", centradaH2[i])
		print("\n")

dev_progressiva(fx)
dev_regressiva(fx)
dev_centrada(fx)