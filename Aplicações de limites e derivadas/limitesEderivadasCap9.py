# Aplicações de limites e derivadas

#bibliotecas

import numpy as np #calculo numerico
import sympy as smp # calculo de limites e derivadas
import matplotlib.pyplot as plt #graficos

# Limites
def limites():
        
    x = smp.Symbol('x')

    funcao = ((x**2 + x -2)/(x-1))
    print(funcao)

    limite = smp.limit(funcao, x, 1)
    print(limite)

    grafico = smp.plot(funcao)

#limites()

#regressão logistica

x= smp.Symbol('x')

FuncaoLog= 1/(1+smp.exp(-x)) #exp = exponencial
print(FuncaoLog)


#limite da função quando x tende a 0

xiszero = smp.limit(FuncaoLog, x, 0)
print(xiszero)

#limite da função quando x tende ao infinito

xisInfinito = smp.limit(FuncaoLog, x, smp.oo)
#print= (xisInfinito)

#limite da função quando x tende ao infinito negativo

xisInfinitoNegativo = smp.limit(FuncaoLog, x, -smp.oo)
#print= (xisInfinitoNegativo)

#derivadas

x = smp.Symbol('x')

funcao = x**2
print(funcao)

DERIVADAS = smp.diff(funcao) #diff igual diferença mas em português refere-se a derivadas
print(DERIVADAS) 

# a derivada de x**2 é 2*x

#graficos

f_original = x**2
f_derivada = smp.diff(f_original)


#tranformar mat simbolica em mat computacional com lambdify

f_original = smp.lambdify(x, f_original)
f_derivada = smp.lambdify(x, f_derivada)

print(f_original(2))

# gráfico da função original
y = [f_original(i) for i in range(-100,100)]
plt.plot(y)
plt.show()

#gráfico da função derivada

y_d = [f_derivada(i) for i in range(-100,100)]
plt.plot(y_d)
plt.show()

