#primeiro passo para realisar uma análise de dados é entender as caracteristicas
# desse dados através das medidas descritivas  #

# ESTATISTICAS DESCRITIVAS

import numpy as np #analise numerica
import pandas as pd  #analise de dados

df_dados_paises = pd.read_csv('csv_Atividade cap 11 dados_1997_2011_paises.csv.csv',
                                sep = ';', 
                                decimal = ',', 
                                 encoding = 'latin1')

print(df_dados_paises.head(10))

# TIPO DAS VARIAVEIS

print(df_dados_paises.dtypes)

#CONTAGEM DOS PAISES

print(df_dados_paises.groupby('pais')\
      .agg(n = pd.NamedAgg('pais', 'count'))\
        .reset_index()) # agregation 


# métricas - medidas de posição

# MEDIDAS DESCRITIVAS - POSIÇÃO

print(df_dados_paises.groupby('pais')\
  .agg(min_idh = pd.NamedAgg('idh','min'),
       max_idh =pd.NamedAgg('idh', 'max'),
       media_idh = pd.NamedAgg('idh', 'mean'))\
       .reset_index())

print('         PRÁTICA')
print(df_dados_paises.groupby('pais')\
      .agg(media_corrup = pd.NamedAgg('corrupcao_indice', 'mean'))\
           .reset_index())

#MODA

print(df_dados_paises.groupby('pais')['idh']\
      .apply(lambda x: x.mode().iloc[0])\
        .to_frame()\
          .reset_index())

print('         PRÁTICA')
print(df_dados_paises.groupby('pais')['corrupcao_indice']\
      .apply(lambda x: x.mode().loc[0])\
        .to_frame()\
          .reset_index())

# MEDIANA

print(df_dados_paises.groupby('pais')\
      .agg(median_idh = pd.NamedAgg('idh', 'median'))\
        .reset_index())


print('     PRÁTICA')
print(df_dados_paises.groupby('pais')\
      .agg(median_corrup = pd.NamedAgg('corrupcao_indice', 'median'))
      .reset_index())

# PERCENTIES / QUARTIES
dados = np.repeat([1,2,3,4,5],2)
print(dados)
print(np.quantile(dados, 0.35))

print(df_dados_paises.groupby('pais')['idh']\
      .apply(lambda x: x.quantile([0.05, 0.25, 0.75, 0.95]))\
      .to_frame()\
      .reset_index()\
      .rename(columns={'level_1': 'percentil'}))


#código mais curto sem usar apply e lambda
print(df_dados_paises.groupby('pais')['idh']
      .quantile([0.05, 0.25,0.75,0.95])
          .reset_index()\
            .rename(columns={'level_1': 'percentil'}))

# MEDIDAS DE VARIABILIDADE

# desvio médio absoluto verificar se os dados estão muito longe do esperado ou não 

print(df_dados_paises.groupby('pais')['idh']\
        .apply(lambda x: (x -x.mean()).abs().mean())\
        .reset_index())

print('         PRÁTICA')
print(df_dados_paises.groupby('pais')['corrupcao_indice']\
  .apply(lambda x : (x - x.mean()).abs().mean())\
  .reset_index())


#variancia e desvio padrão

print(df_dados_paises.groupby('pais')\
      .agg(variancia_idh = pd.NamedAgg('idh', 'var'), 
           dp_idh =pd.NamedAgg('idh','std'))\
          . reset_index())