import csv
import pandas as pd
import numpy as np
import random as random

dataframe = pd.read_csv('dataframe.csv')
#print(dataframe)

# 1. Quantos alunos do sexo masculino e feminino estão na amostra?
print('#Identifique qual q relação de alunos de sexo masculino e feminino no conjunto.')
print(dataframe['Sexo'].value_counts())
print(dataframe['Sexo'].value_counts(normalize=True)*100)
print("-"*20)
#print(dataframe['Idade'].value_counts())
#grupo_idade = pd.cut(dataframe['Idade'], bins=[0, 20, 30, 40, 50, 60, 70, 80, 90], labels=['0-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90'])

#print(grupo_idade.value_counts())
#grupo_idade_enem=dataframe.groupby(pd.cut(dataframe['Idade'], bins=[0, 20, 30, 40, 50, 60, 70, 80, 90], labels=['0-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90']))['ENEM'].mean()
print('#Dado que os alunos tem idade entre 18 e 28 anos, mostre qual a média da nota do ENEM dos alunos agrupados por idade.')
grupo_idade_enem=dataframe.groupby('Idade')['ENEM'].mean()
print(grupo_idade_enem)
print("-"*20)

print('Normalize as notas do ENEM de todos os alunos para um valor entre 5 e 10.')
norm= (dataframe['ENEM']/dataframe['ENEM'].abs().max())*5+5
print(norm)

print('Foi criada coluna ENEM Norm com as notas do ENEM normalizadas.')
dataframe['ENEM Norm']=norm

#print(dataframe['ENEM'].abs().max())
#print(dataframe['ENEM'].abs().min())
#print(norm.min()*5+5)
print('top 10 ENEM Norm Feminino') #poderia ter pegado a coluna ENEM Norm
notaFemininoEnem=dataframe[dataframe['Sexo']=='F']['ENEM'].sort_values(ascending=False)[:10]
print(notaFemininoEnem)
norm_notaFemininoEnem=(notaFemininoEnem/notaFemininoEnem.abs().max())*5+5
print(norm_notaFemininoEnem)

print('Topo 10 ENEM Norm Masculino') #poderia ter pegado a coluna ENEM Norm
notaMasculinoEnem=dataframe[dataframe['Sexo']=='M']['ENEM'].sort_values(ascending=False)[:10]
print(notaMasculinoEnem)
norm_notaMasculinoEnem=(notaMasculinoEnem/notaMasculinoEnem.abs().max())*5+5
print(norm_notaMasculinoEnem)

print('Mostre os 10 alunos do sexo feminino com as maiores notas no CRA6.')
cra6Feminino=dataframe[dataframe['Sexo']=='F']['CRA_apos6'].sort_values(ascending=False)[:10]
print(cra6Feminino)

print('Mostre os 10 alunos do sexo masculino com as maiores notas no CRA6.')
cra6Masculino=dataframe[dataframe['Sexo']=='M']['CRA_apos6'].sort_values(ascending=False)[:10]
print(cra6Masculino)

print('Slice do dataframe com as 10 Femininos com maiores notas no CRA6.')
loc10Feminino=cra6Feminino.index
#print(loc10Feminino)
#print(dataframe.loc[loc10Feminino,('ENEM','ENEM Norm','CRA_apos2','CRA_apos4','CRA_apos6')])
sliceTop10Feminino = dataframe.loc[loc10Feminino,('ENEM Norm','CRA_apos2','CRA_apos4','CRA_apos6')]
print(sliceTop10Feminino)
print(sliceTop10Feminino.index)

print('Slice do dataframe com as 10 Masculinos com maiores notas no CRA6.')
#locMasc=dataframe[dataframe['Sexo']=='M'].loc[dataframe['CRA_apos6'].idxmax()]
loc10Masc=cra6Masculino.index
#print(loc10Masc)
#print(dataframe.loc[loc10Masc,('ENEM','ENEM Norm','CRA_apos2','CRA_apos4','CRA_apos6')])
sliceTop10Masc = dataframe.loc[loc10Masc,('ENEM Norm','CRA_apos2','CRA_apos4','CRA_apos6')]
print(sliceTop10Masc)
print(sliceTop10Masc.index)
print('Plot grafico de dispersão entre ENEM e CRA_apos6.') 
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('classic')

#print(sliceTop10Feminino.iloc[0])
#print(sliceTop10Feminino.loc)

llegend=[sliceTop10Feminino.index, sliceTop10Masc.index]
fig = plt.figure(figsize=(20,30))
#fig.figwidth(10)
#fig.figheight(10)

#legend(llegend)


#ax.plot(sliceTop10Feminino.columns, sliceTop10Feminino.index)
#plt.show()
for i in range(10):


    plt.plot(sliceTop10Feminino.columns,sliceTop10Feminino.iloc[i], '-o', label=sliceTop10Feminino.index[i], linewidth=2)    
    plt.plot(sliceTop10Masc.columns,sliceTop10Masc.iloc[i], '-s', label=sliceTop10Masc.index[i])

plt.xlim(-1, 4)
plt.grid(True)
plt.legend(loc='best')
plt.show()

#sns.scatterplot(dataframe['ENEM Norm'], dataframe['CRA_apos2'], dataframe['CRA_apos4'], dataframe['CRA_apos6'], hue=dataframe['Sexo'])'''