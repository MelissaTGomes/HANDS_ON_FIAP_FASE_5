import numpy as np #calculo numerico
import sympy as smp ##limites, derivados e integrais
import pandas as pd #analise de dados
import matplotlib.pyplot as plt #graficos

def area_aproximada():
    x = smp.Symbol('x')
    f = 2*x**2  #define a altura do gráfico
    print(f)

    smp.integrate(f) #função para calcular integral no python

    #intervalo
    minimo = 0
    maximo = 24
    n = 8

    #tamanho dos intervalos (base)
    dx = (maximo - minimo ) / n
    print(dx) 

    #transformar a função para ser utilizada em operações
    x = smp.Symbol('x')
    f = 2*x**2 #define a altura do gráfico
    f_x = smp.lambdify(x, f)

    # criar a sequencia para o eixo x
    eixo_x = np.arange(minimo, maximo+dx, dx)

    #criar sequencia para eixo y
    eixo_y = [float(f_x(i)) for i in eixo_x]
    # o loop 'for i in' irá procurar os valores de i na variavel 'eixo_x'
    # e irá realizar o calculo 2x**2 dos valores encontrados, ou seja se em eixo x o primeiro valor for 3 
    # ele irá calcular 2*3**2, dessa forma teremos a altura do retangulo###

    print(f"eixoX {eixo_x}") 
    print(f"eixoY {eixo_y}")

    #criar gráfico
    plt.bar(x = eixo_x, height = eixo_y, width=2)#grafico de barras
    plt.plot(eixo_x, eixo_y, color='red')#grafico de linha
    #plt.show()

    #Area do retangulo (multiplicar base vezes altura) 
    fx_dx = [i*dx for i in eixo_y]
    print(fx_dx)

    area_aprox= sum(fx_dx) #area aproximada
    print(area_aprox)

#area_aproximada()

def calculo_integral():

    x= smp.Symbol('x')
    f = 2*x**2
    funcao_integral = smp.integrate(f)
    print(funcao_integral)

    #tranformação em uma função computacional para o python poder calcular
    f_x = smp.lambdify(x, funcao_integral) 

    #calculo de integrais: area do maximo - area do minimo
    integral = f_x(24) - f_x(0)
    print(integral)

#calculo_integral()    

x = smp.Symbol('x')
f = 2*x**2  #define a altura do gráfico
print(f)

smp.integrate(f) #função para calcular integral no python

#intervalo
minimo = 0
maximo = 24
n = 8

#tamanho dos intervalos (base)
dx = (maximo - minimo ) / n
print(dx) 

#transformar a função para ser utilizada em operações
x = smp.Symbol('x')
f =2*x**2 #define a altura do gráfico
f_x = smp.lambdify(x, f)

# criar a sequencia para o eixo x
eixo_x = np.arange(minimo, maximo+dx, dx)

#criar sequencia para eixo y
eixo_y = [float(f_x(i)) for i in eixo_x]
# o loop 'for i in' irá procurar os valores de i na variavel 'eixo_x'
# e irá realizar o calculo 2x**2 dos valores encontrados, ou seja se em eixo x o primeiro valor for 3 
# ele irá calcular 2*3**2, dessa forma teremos a altura do retangulo###

print(f"eixoX {eixo_x}") 
print(f"eixoY {eixo_y}")

#criar gráfico
plt.bar(x = eixo_x, height = eixo_y, width=2)#grafico de barras
plt.plot(eixo_x, eixo_y, color='red')#grafico de linha
#plt.show()

#Area do retangulo (multiplicar base vezes altura) 
fx_dx = [i*dx for i in eixo_y]
print(fx_dx)

area_aprox= sum(fx_dx) #area aproximada
print(area_aprox)

x= smp.Symbol('x')
f = 2*x**2
funcao_integral = smp.integrate(f)
print(funcao_integral)

#tranformação em uma função computacional para o python poder calcular
f_x = smp.lambdify(x, funcao_integral) 

#calculo de integrais: area do maximo - area do minimo
integral = f_x(24) - f_x(0)
print(integral)
#diferença da area aproxima e da area integral 

diferenca = area_aprox - integral 
print(diferenca)

#simplificando a função integral

x = smp.Symbol('x')
f = 2*x**2
int =smp.integrate(f, (x, minimo, maximo))
print(int)
