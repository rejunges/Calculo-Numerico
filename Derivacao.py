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

import argparse
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.linalg import lu_factor, lu_solve

# Leitura dos argumentos por linha de comando
ap = argparse.ArgumentParser()
ap.add_argument('-x', "--x", required=True, help="Entrada x")
ap.add_argument('-h', "--h", required=True, help="Entrada h")
ap.add_argument('-f', "--f", required=True, nargs='+', help="Função")


