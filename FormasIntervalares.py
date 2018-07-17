"""
Derivação por formulas de diferenças divididas

Desenvolvido por:
	- Karine Pestana
	- Marcelo Bonoto
	- Renata Junges

Disciplina: 
	Cálculo Numérico Computacional 2018-1

Argumentos:
	-x: Intervalo
	-f(x): função 
	-r: raiz
"""

#python3 FormasIntervalares.py -f 100*(x**2)-5 -x 0.1 10 -r 0.22360679


import argparse
import matplotlib.pyplot as plt
import numpy as np
import math
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

# Leitura dos argumentos por linha de comando
ap = argparse.ArgumentParser()
ap.add_argument('-f', "--f", required=True, help="Funcao")
ap.add_argument('-x', "--x", required=True, nargs='+', help="Valores do intervalo")
ap.add_argument('-r', "--r", required=True, help="Raiz")


args = vars(ap.parse_args())
x = list(map(float, args["x"]))
funcao = args["f"]
r = float(args["r"])


print("\n ---------------------------- Entradas ----------------------------\n")
print("Intervalo:", x)
print("Função:", funcao)
print("Raiz:", r)


#calcula a derivada primeira de qualquer funcao e retorna seu valor
def derivada(func, x):
	y = Symbol("x")
	f = parse_expr(func)
	dev = diff(f,y,1)
	
	dev = dev.subs(y, x).doit() 

	return dev

derivadaprimeira = derivada(funcao, r)
print(derivadaprimeira)

