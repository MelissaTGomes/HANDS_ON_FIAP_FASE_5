import pandas as pd
import numpy as np
import sympy as smp
import matplotlib.pyplot as plt 

#dados
minimo = -50
maximo = 50
n = 10

#definir base

dx = maximo - minimo / n
print(dx)

#converter função para calculo em python

x = smp.Symbol('x')
f = 3*x**2 + x**2
f_x= smp.lambdify(x,f)

#criando sequencia do eixo x
eixoY = np.arange(minimo, maximo+dx, dx)

#criando sequecia para eixo y

eixoX = [int(f_x(i)) for i in eixoY]

print(eixoX)
print(eixoY)

plt.bar(x = eixoX, height = eixoY, width=1)#grafico de barras
plt.plot(eixoX, eixoY, color='red')
plt.show()






