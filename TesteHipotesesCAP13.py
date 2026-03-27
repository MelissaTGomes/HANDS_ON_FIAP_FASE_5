#gerais
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Analises
from scipy import stats as st
import pingouin as pg #ferramenta de teste de hipoteses


dados_nps = pd.read_csv('csv_nps_example.csv', sep =';', encoding= 'utf8')
dados_ab = pd.read_csv('csv_exampleDataABtest.csv')

print(dados_ab.head(),'\n')
print(dados_nps.head(),'\n')


#TESTE T

print(dados_ab.groupby('group')\
    .agg(media_ab = pd.NamedAgg('clickedTrue', 'mean'),
         dp_ab = pd.NamedAgg('clickedTrue', 'std'),
         n = pd.NamedAgg('clickedTrue', 'count')).reset_index(),'\n')

gr_A = dados_ab[dados_ab ['group'] == 'A']['clickedTrue']
gr_B = dados_ab[dados_ab['group'] == 'B']['clickedTrue']

print('GRUPO A', '\n', gr_A, '\n','GRUPO B', '\n', gr_B,'\n')

## TESTE T NO SCIPY

print(st.ttest_ind(gr_A, gr_B, alternative = 'two-sided'),'\n')

#se o p-value < 0.05 - então rejeito a hipotese nula

## TESTE T NO PINGOUIN

print(pg.ttest(x=gr_A, y = gr_B, alternative='two-sided', confidence= 0.95),'\n')

#se o p-value < 0.05 - então rejeito a hipotese nula


# TESTE F

#verificar as respostas 

print(dados_nps.groupby('response_status')\
    .size()\
        .to_frame('n')\
        .reset_index())

#verificar valores nulos

#print(dados_nps[dados_nps['nps_score'].isnull()]) 

##variavel[variavel[coluna].énulo()]

dados_nps_filtrados = dados_nps[(dados_nps['response_status'] == 'Complete') & \
                                (dados_nps['nps_score'].notna())]

print(dados_nps_filtrados.head())

#verificar grupo foco


dados_nps_filtrados.groupby('age')\
    .agg(media_nps = pd.NamedAgg('nps_score', 'mean'))