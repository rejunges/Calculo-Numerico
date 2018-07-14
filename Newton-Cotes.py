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

#python3 Newton-Cotes.py -x 1 0.5 -f "x**3" -r 1
#python3 Newton-Cotes.py -x 0.5 0 -f "2/(x-4)" -r 2
#python3 Newton-Cotes.py -x 0 2 1 1 -f "(x**2*e**(x**2))" -r 3


import argparse
import matplotlib.pyplot as plt
import numpy as np
import math
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

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

	#trapezio = np.trapz(y, x)
	
	#trapezio calculado com a formula
	h = x[1] - x[0]
	trapezioB = (h/2)*(y[0] + y[1]) 

	#erro do trapezio 
	y = Symbol("x")
	f = parse_expr(funcao)
	derivada = diff(f,y,2)
	#print(derivada)#printa a formula da derivada da funcao

	eT = -(pow(h,3)/12) - derivada.subs(y, (x[0] + x[1])/2).doit() #utiliza derivada segunda com o valor de c(média entre x0 e x1) 
	print("Regra Trapézio:", trapezioB)
	print("Erro to Trapézio: ", eT)
	
def regra_simpson(x):
	y = []
	x_linha = []
	i = 0

	#calculo a distância de cada intervalo
	h = round((x[1] - x[0])/2, 2)

	x_linha.append(x[0])
	x_linha.append(x[0]+h)
	x_linha.append(x[1])

	i = 0
	for i in range(0, len(x_linha)):
		y.append(eval(funcao.replace("x", str(x_linha[i]))))	

	simpson = (h/3)*(y[0] + 4*y[1] + y[2]) 

	print("Regra Simpson:", simpson)
	

def regra_romberg(x):
	return 0

if (r == 1):
	regra_trapezio(x)
elif(r == 2):
	regra_simpson(x)
elif(r == 3):
	regra_romberg(x)
