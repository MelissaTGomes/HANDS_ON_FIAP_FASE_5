import pandas as pd
import numpy as np
import random as rd #obter números aleatórios
from sklearn.model_selection import train_test_split #uutilizado em machine learning para dividir os dados em train e test 
#vamos utilizar para realizar amostrageeem estratificada

dados_renda_municipios = pd.read_csv('csv_dados_renda_municipios.csv',
                                     sep = ',',
                                     decimal = '.',
                                     encoding = 'utf-8'
                                     )

print(dados_renda_municipios.head(10))

#tamanho dos dados
print(dados_renda_municipios.shape)

#Iremos utilizar os dados do censo ccomo parâmetros de amostra piloto

#Escolher UF

dados_municipio = dados_renda_municipios[dados_renda_municipios['UF'] == 'São Paulo'].reset_index(drop=True)      
print(dados_municipio)

print(dados_municipio.shape)

#CRIAR EXTRATOS

dados_municipio['classe_renda']= pd.qcut(dados_municipio['RDPC'], 4, labels = ['D','C','B','A'])

print(dados_municipio)

#AMOSTRA PILOTO

dados_piloto =dados_municipio.agg(media_rdpc = pd.NamedAgg('RDPC', 'mean'),
                          dp_rdpc = pd.NamedAgg('RDPC', 'std'),
                          qnt = pd.NamedAgg('RDPC', 'count'))
print(dados_piloto)

#dados piloto por extrato

dados_piloto_classe = dados_municipio.groupby('classe_renda')\
                                              .agg(media_rdpc= pd.NamedAgg('RDPC', 'mean'),
                                                   dp_rdpc= pd.NamedAgg('RDPC', 'std'),
                                                   N = pd.NamedAgg('RDPC', 'count'))\
                                                   .reset_index()

print(dados_piloto_classe)


def formula_amostra_discreta(N, Z, ME):
    N = (Z**2 * 0.25 * N) / ((ME**2 * (N-1)) + (Z**2 * 0.25))
    return int(N)
    #formula discreta - descobrir o tamanho da amostra 
    #Fórmulas Discretas: Para dados contáveis (ex.: número de alunos).

# N = população
# ME = Margem de erro
# Z = Nivel de confiança
# s = variância (desvio padrão ao quadrado dp**2)
 
def formula_amostra_continua(N, S, Z, ME):
    N = (Z**2 * S**2 * N) / ((ME**2 * (N-1)) + (Z**2 * S**2))
    return int(N)
    #formula continua - descobrir o tamanho da amostra 
    #Fórmulas Contínuas: Para dados mensuráveis frações e decimais (ex.: altura).
    #As distribuições contínuas são usadas quando os dados podem assumir qualquer valor em um intervalo.

##USO DA FORMULA 

#parametros

N = 645
Z = 1.96
S = 197.40
ME = 25

n = formula_amostra_continua(N, S, Z, ME)
print(n) #neste caso minha amostra é 174 de 645mil

#METODOS DE AMOSTRAGEM 

#AMOSTRA ALEATÓRIA SIMPLES

#-FUNÇÃO RANDOM - sorteio de linhas

linhasSorteadas = rd.sample(range(1, N+1), n)  #aqui será sorteado aleatoriamente 174 casos dentre os 645 mil para criar a amostra 
print(linhasSorteadas)

print(len(linhasSorteadas))

#filtrar dados 

dadosAmostra = dados_municipio[dados_municipio.index.isin(linhasSorteadas)]
#vai buscar os números sorteados dentro de dados municipios, index está transformando esse dados em um dataframe 

print(dadosAmostra)

#-FUNÇÃO SAMPLE - sorteio de linhas 

DadosAmostraSimples = dados_municipio.sample(n=n) #realiza sorteio aleatório diretamente sem criar números aleatórios
print(DadosAmostraSimples.shape)
 
# AMOSTRA ESTRATIFICADA

dadosAmostraEstrat = train_test_split(dados_municipio,
                                      test_size=n,
                                      random_state=1245,#utilizar random_state para sortear sempre os mesmos dados
                                      stratify=dados_municipio['classe_renda'])[1] #indice [0] são para dados de treino e indice [1] para dados de teste

print(dadosAmostraEstrat)

#pergunta: Existe uma diferença significativa enre os dados da amostra (174) e os dados da população (645mil)?

#pra isso vamos realizar a avaliação

#AVALIAÇÃO

print(dados_piloto, '\n',
       dados_piloto_classe)

print(DadosAmostraSimples.agg(media_RDPC = pd.NamedAgg('RDPC', 'mean'),
                        dp_RDPC = pd.NamedAgg('RDPC', 'std'),
                        total = pd.NamedAgg('RDPC', 'count')).reset_index())

print(dadosAmostraEstrat.groupby('classe_renda', observed =True)\
      .agg(media_RDPC = pd.NamedAgg('RDPC', 'mean'),
           dp_RDPC = pd.NamedAgg('RDPC', 'std'),
           total = pd.NamedAgg('RDPC', 'count'))
                 .reset_index(), '\n', dados_piloto_classe)

def funcao_MAD(x):
    (x - x.mean()).abs().mean()