import numpy as np

import pandas as pd

import sympy

dataframe = pd.read_csv("/planilha.csv")

colx = dataframe["Quantidade de Vendas"]

coly = dataframe["Salário"]

n = len(colx)

x2 = np.power(colx,2)

x3 = np.power(colx,3)

x4 = np.power(colx,4)

xy = np.multiply(colx,coly)

x2y = np.multiply(x2,coly)

sx1 = np.sum(colx)

sx2 = np.sum(x2)

sx3 = np.sum(x3)

sx4 = np.sum(x4)

sxy = np.sum(xy)

sx2y = np.sum(x2y)

sy = np.sum(coly)
 
matriz1 = sympy.Matrix([[n,sx1,sx2],[sx1,sx2,sx3],[sx2,sx3,sx4]])
matriz2 = sympy.Matrix([[n,sx1,sx2],[sx1,sx2,sx3],[sx2,sx3,sx4]])
matriz3 = sympy.Matrix([[n,sx1,sx2],[sx1,sx2,sx3],[sx2,sx3,sx4]])
matriz4 = sympy.Matrix([[n,sx1,sx2],[sx1,sx2,sx3],[sx2,sx3,sx4]])

matriz2[:,0] = [sy,sxy,sx2y]

matriz3[:,1] = [sy,sxy,sx2y]

matriz4[:,2] = [sy,sxy,sx2y]

det = matriz1.det()

det1 = matriz2.det()

det2 = matriz3.det()

det3 = matriz4.det()

c = float(det1/det)

b = float(det2/det)

a = float(det3/det)

y = print(a,"* x2 + ",b," * x + ",+ c)
