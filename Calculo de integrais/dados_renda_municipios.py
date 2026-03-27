import numpy as np
import sympy as smp
import pandas as pd
import matplotlib.pyplot as plt

dados_municipios = pd.read_csv(
    'csv_DADOS_RENDA_MUNICIPIO333.csv', 
    encoding='latin1',
    sep = ';')
print(dados_municipios.head())

#encontrar integral da função
x = smp.Symbol('x')
f = 2*x**2
cal_integ = smp.integrate(f)
print(cal_integ)

minimo = dados_municipios['RDPC'].min()
maximo = dados_municipios['RDPC'].max()

print(minimo, maximo)

x = smp.Symbol('x')
f = 2*x**2
int =smp.integrate(f, (x, minimo, maximo))
print(int)

dados_ordenados = dados_municipios.sort_values(by='RDPC')

plt.bar(x = dados_municipios['municipio'], height = dados_ordenados['RDPC'], width= 0.3)
plt.plot(dados_municipios['municipio'], dados_ordenados['RDPC'], color='k')
plt.show()

# intervalo
##fx_dx = [i*dx for i in dados_ordenados]
#sum(fx_dx)