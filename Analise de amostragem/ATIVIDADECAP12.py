import pandas as pd
import numpy as np 
import random as rd
from sklearn.model_selection import train_test_split


dados_renda_municipios = pd.read_csv('csv_dados_renda_municipios.csv',
                               sep = ',',
                               decimal= '.',
                               encoding= 'utf-8')

print(dados_renda_municipios.head())

print(dados_renda_municipios.shape)

#filtrar dados (a)

dados_municipios = dados_renda_municipios[dados_renda_municipios['UF'] == 'Bahia'].reset_index(drop=True)
#definir variavel = DadosCarregados [DadosCarregados['colunaa ser filtrada'] == 'valor a ser filtrado'].reset_index('pare quando achar o valor')
print(dados_municipios)

#dados piloto (b)

DadosPilotos = dados_municipios.agg(media_rdpc = pd.NamedAgg('RDPC', 'mean'),
    mediana_rdpc = pd.NamedAgg('RDPC', 'median'),
    dp_rdpc = pd.NamedAgg('RDPC', 'std'),
    total= pd.NamedAgg('RDPC', 'count')).reset_index()
print(DadosPilotos)

# Calcular tamanho da amostra

def TamanhoAmostra(N, S, Z, ME):
    N = (Z**2 * S**2 * N) / ((ME**2 * (N-1)) + (Z**2 * S**2))
    
    return int(N)

#Calcular tamanho da amostra (c)

N = 417
ME = 15
Z = 1.96
S = 101.93

n = TamanhoAmostra(N,S,Z,ME)
print(n)

#amostra aleatoria simples (d)
AmostraAleatoriaSimples = dados_municipios.sample(n)
print(AmostraAleatoriaSimples)

AAS = AmostraAleatoriaSimples.agg(media_rdpc = pd.NamedAgg('RDPC', 'mean'),
        mediana_rdpc = pd.NamedAgg('RDPC', 'median'),
        dp_rdpc = pd.NamedAgg('RDPC', 'std')).reset_index()

print('AMOSTRA SIMPLES', '\n', AAS, '\n', 'DADOS PILOTO', '\n', DadosPilotos)

