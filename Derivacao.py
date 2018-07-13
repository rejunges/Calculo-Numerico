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
h = args["h"]
f = args["f"]

print("X: ", x)
print("H: ", h)
print("F: ", f)

fx = []

def progressiva(fx):
	return 0


