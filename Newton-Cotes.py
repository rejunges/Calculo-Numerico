"""
Derivação por formulas de diferenças divididas

Desenvolvido por:
	- Karine Pestana
	- Marcelo Bonoto
	- Renata Junges

Disciplina: 
	Cálculo Numérico Computacional 2018-1

Argumentos:
	-x: Valores de x
	-f(x): função 
	-r: 
		1 para Trapézio
		2 para Simpson
		3 para Romberg
"""

#python3 Newton-Cotes.py -x 1 0.5 "-f" "pow(x,4)" -r 1
#python3 Newton-Cotes.py -x 0.5 0 1 "-f" "2/x-4" -r 2
#python3 Newton-Cotes.py -x 0 2 1 1 "-f" "pow(x,2)*pow(e,pow(x,2))" -r 3


import argparse
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.linalg import lu_factor, lu_solve

# Leitura dos argumentos por linha de comando
ap = argparse.ArgumentParser()
ap.add_argument('-x', "--x", required=True, nargs='+', help="Valores de x")
ap.add_argument('-f', "--f", required=True, help="Funcao")
ap.add_argument('-r', "--r", required=True, help="Regra: 1-trapézio; 2-simpson; 3-romberg")

args = vars(ap.parse_args())
x = list(map(float, args["x"]))
funcao = args["f"]
r = int(args["r"])

print("\n ---------------------------- Entradas ----------------------------\n")
print("X:", x)
print("Função:", funcao)
print("Regra:", r)

def regra_trapezio(x):
	y = []
	i = 0
	for i in range(0, len(x)):
		y.append(eval(funcao.replace("x", str(x[i]))))

	trapezio = np.trapz(y, x)
	print("Regra Trapézio:", trapezio)

def regra_simpson(x):
	return 0

def regra_romberg(x):
	return 0


if (r == 1):
	regra_trapezio(x)
elif(r == 2):
	regra_simpson(x)
elif(r == 3):
	regra_romberg(x)
