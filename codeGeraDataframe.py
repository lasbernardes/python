import csv
import numpy as np
import pandas as pd
import random as random
from faker import Faker
fake = Faker('pt_BR')

#criação de series

# Criação
sexo=[]
nome=[]
for i in range(1000):
    sexo.append(random.choice(['M', 'F']))
    if sexo[i] == 'M':
        nome.append(fake.name_male())
    else:
        nome.append(fake.name_female())

#for i in range(1000):
##    print(sexoMasc[i], nome[i])

cpf=[]
for i in range(1000):
    cpf.append(fake.cpf())
#print(cpf)

idade=[]
for i in range(1000):
    idade.append(random.randint(18, 28))
#print(idade)

email=[]
for i in range(1000):
    email.append(fake.email())
#print(email)

enem=[]
for i in range(1000):
    enem.append(random.randint(640, 800))
#print(enem)

abandono=[]
abandonoSemestre=np.full((1000), np.nan)
cra_apos2=np.full((1000), np.nan)
cra_apos4=np.full((1000), np.nan)
cra_apos6=np.full((1000), np.nan)

for i in range(1000):
    abandono.append(random.choice([True, False]))

#print(abandono)
for i in range(1000):
    
    if abandono[i] == True:
        #print(abandono[i],":",str(i))
        abandonoSemestre[i] = random.randint(1, 7)
        if abandonoSemestre[i] >2:
            cra_apos2[i] = random.uniform(5, 10)
        else: 
            cra_apos2[i] = 0
        
        if abandonoSemestre[i] > 4:#  and abandonoSemestre[i] <= 4:
            cra_apos4[i] = random.uniform(5, 10)
        else:
            cra_apos4[i] = 0

        if abandonoSemestre[i] > 6:#4 and abandonoSemestre[i] <= 6:
            cra_apos6[i] = random.uniform(5, 10)
        else:
            cra_apos6[i] = 0
    else:
        #print(i)
        abandonoSemestre[i] = 0
        cra_apos2[i] = random.uniform(5, 10)
        cra_apos4[i] = random.uniform(5, 10)
        cra_apos6[i] = random.uniform(5, 10)

#print(abandono)

dataframe=pd.DataFrame({'Nome':nome, 'Sexo':sexo, 'CPF':cpf, 'Idade':idade, 'Email':email, 'ENEM':enem, 'Abandono':abandono, 'AbandonoSemestre':abandonoSemestre, 'CRA_apos2':cra_apos2, 'CRA_apos4':cra_apos4, 'CRA_apos6':cra_apos6})

print(dataframe)
dataframe.to_csv('dataframe.csv', index=False)

'''

sAbandono= pd.Series(random.choice([True, False]) for i in range(1000))
print(sAbandono)
for i in sAbandono:
    if i == True:
        print(sAbandono.loc(i))
        #sAbandonoSemestre = pd.Series(pd.loc[random.randint(1, 7))
        #df.loc[row_number] = row_value
    else:
        sAbandonoSemestre = pd.Series(0 for i in range(1000))
print(sAbandonoSemestre)
#sAbandonoSemestre= pd.Series(random.uniform(1, 7) for i in range(1000))
sCRA_pos2 = pd.Series(random.uniform(5, 10) for i in range(1000))
#print(sCRA_pos2)
sCRA_pos4 = pd.Series(random.uniform(5, 10) for i in range(1000))
#print(sCRA_pos4)
sCRA_pos6 = pd.Series(random.uniform(5, 10) for i in range(1000))
#print(sCRA_pos6)


# Criação de um dataframe
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})'''