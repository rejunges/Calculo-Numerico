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
	-n: quantos valores sao usados na coluna K (romberg)
"""

#python3 Newton-Cotes.py -x 1 0.5 -f "x**4" -r 1
#python3 Newton-Cotes.py -x 0.5 0 -f "(2/(x-4))" -r 2
#python3 Newton-Cotes.py -x 0 2 -f "(x**2*(e**(x**2)))" -r 3 -n 6 
#python3 Newton-Cotes.py -x 0 2 -f "(e**(x**2))" -r 3 -n 3 

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
ap.add_argument('-n', "--n", required=False, help="Quantos valores serao usados na coluna K=0 até K=n-1 (Romberg)")

args = vars(ap.parse_args())
x = list(map(float, args["x"]))
funcao = args["f"]
r = int(args["r"])

if (r == 3):
	n = int(args["n"])

print("\n ---------------------------- Entradas ----------------------------\n")
print("X:", x)
print("Função:", funcao)
print("Regra:", r)

def trap_romb(x, h, funcao):
	y = []
	
	funcao = funcao.replace("e", "2.718") #substitui o valor de e pela exponencial (se houver)
	for i in range(0, len(x)):
		y.append(eval(funcao.replace("x", str(x[i]))))

	#trapezio = np.trapz(y, x)
	
	#trapezio calculado com a formula
	trapezio = (h/2)*(y[0] + y[1]) 

	#se for a regra de romberg que chama esse método entao retorna o valor de trapezio
	return trapezio 

def regra_trapezio(x):
	y = []
	
	for i in range(0, len(x)):
		y.append(eval(funcao.replace("x", str(x[i]))))

	#trapezio = np.trapz(y, x)
	
	#trapezio calculado com a formula
	h = x[1] - x[0] #calcula h apenas se 
	trapezioB = (h/2)*(y[0] + y[1]) 

	#erro do trapezio 
	y = Symbol("x")
	f = parse_expr(funcao)
	derivada = diff(f,y,2)
	#print(derivada)#printa a formula da derivada da funcao
	eT = -(pow(h,3)/12) - derivada.subs(y, (x[0] + x[1])/2).doit() #utiliza derivada segunda com o valor de c(média entre x0 e x1) 

	print("Regra Trapézio:", trapezioB)
	print("Erro do Trapézio: ", eT)
	
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

	#erro do simpson 
	y = Symbol("x")
	f = parse_expr(funcao)
	derivada = diff(f,y,4)
	eS = -(pow(h,5)/90) - derivada.subs(y, (x[0] + x[1])/2).doit() #utiliza derivada segunda com o valor de c(média entre x0 e x1) 
	
	print("Regra Simpson:", simpson)
	print("Erro do Simpson : ", eS)
	

def regra_romberg(x,n, funcao):
	#Cria matriz de romberg (triangulo superior será 0 e o inferior será o tringulo de romberg)
	R = np.zeros(shape=[n, n])
	h = x[1] - x[0]
	
	R[0][0] = trap_romb(x,h,funcao)
	funcao = funcao.replace("e", "2.718")
	erro = 0
	for i in range(1,n): #linha
		#somatorio pra adicionar no R[i][0]
		somatorio = 0
		hn = h/pow(2,i)
		for j in range(1, pow(2, i-1)):
			xa = x[0] + (2*(j+1) - 1)* hn
			somatorio += eval(funcao.replace("x", str(xa)))
			
		R[i][0] = (1/2)* R[i-1,0] + hn * somatorio
	
	for i in range(1, n): #linha
		hn = h/pow(2,i)
		erro += pow(hn, 2*i +2)
		for j in range(1,i+1): #coluna
			R[i][j] = (1/(pow(4,j)-1)) * (pow(4,j)*R[i, j-1] - R[i-1, j-1])
	
	print("\n-----------------------Matriz Inferior dos valores de Romberg-------------\n")
	print(R)
	print("\n-------------------")
	print("\nMétodo do Romberg: ", R[n-1][n-1])
	print("Erro do Romberg: ", erro)

if (r == 1):
	regra_trapezio(x)
elif(r == 2):
	regra_simpson(x)
elif(r == 3):
	regra_romberg(x,n, funcao)
