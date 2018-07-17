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

#python3 FormasIntervalares.py -f "100*(x**2)-5" -x 0.1 10 -r 0.22360679 #funcionando perfeitamente
#python3 FormasIntervalares.py -f "(1/x)-x-1" -x 0.1 10 -r 0.61803398  #poderia parar na anterior (iteracao 6 de 5)
#python3 FormasIntervalares.py -f "2*x**2 - 5*x -7" -x 2 100 -r 3.5 #vai até a iteracao 9 e deveria parar na 7
#python3 FormasIntervalares.py -f "x" -x -150 100 -r 0 #faz só 1x (corret0)
#python3 FormasIntervalares.py -f "4*x**3-2*x" -x 0.5 3 -r 0.70710678 #vai 1 iteracao além ( iteracao 6 de 5)
#python3 FormasIntervalares.py -f "4*x**3-2*x" -x 0.5 50 -r 0.70710678 #correto (9 iteracoes)


import argparse
import math
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from interval import interval

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
	#print(dev)
	dev = dev.subs(y, x).doit() 

	return dev

#calcula intervalo baseado no valor do intervalo anterior e no valor da função
def calcula_intervalo(intervalo_X, func):
	mid = (x[0] + x[1]) / 2 #media dos valores anteriores
	f_mid = eval(funcao.replace("x", str(mid)))

	x_k = interval[x[0], x[1]]
	N_x = interval[mid, mid] - (interval[f_mid, f_mid])/(interval[derivada(funcao, x[0]), derivada(funcao, x[1])])
	
	return x_k & N_x

i = 0
x = calcula_intervalo(x, funcao)
while r in x and r != x[0].inf:
	i = i + 1
	x = [x[0].inf, x[0].sup]
	#x = [round(x[0].inf,7), round(x[0].sup, 7)]
	print("Iteracao ", i, " ", x)
	x = calcula_intervalo(x, funcao)

#trata o caso de ter apenas uma iteracao
if i == 0:
	print("Iteracao ", i+1, " ", [x[0].inf, x[0].sup])
	
	

