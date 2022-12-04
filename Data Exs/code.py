#Yan D. R. Machado
#LOpEL - PUC-Rio

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#-------------- funcs ---------------

def csvname(N_i, N_f): #cria o nome do arquivo para cada um dos canais
    datalist = []
    for i in range(N_i, N_f+1, 2):
        if i < 10:
            dataname1 = 'tek000' + str(i) + 'CH1.csv'
            dataname2 = 'tek000' + str(i+1) + 'CH2.csv'
        elif i < 100:
            dataname1 = 'tek00' + str(i) + 'CH1.csv'
            dataname2 = 'tek00' + str(i+1) + 'CH2.csv'
        elif i < 1000:
            dataname1 = 'tek0' + str(i) + 'CH1.csv'
            dataname2 = 'tek0' + str(i+1) + 'CH2.csv'
            
        datalist.append((dataname1,dataname2))
        
    return datalist #termina com uma lista com os arquivos dentro do intervalo numérico

def datacleaner(dataset1,dataset2,headersize): #tira o header do .csv (menos o diretamente acima)
    dataset1 = pd.read_csv(dataset1, header = headersize)
    dataset2 = pd.read_csv(dataset2, header = headersize)
    return dataset1, dataset2

def defaxis(dataset,header): #define o eixo baseado no header logo acima 
    axis = dataset[header].tolist()
    return axis

def plotdata(dataname1,dataname2): #faz o plot dos canais sobrepostos
    X = defaxis(dataname1,'TIME')
    Y1 = defaxis(dataname1, 'CH1')
    Y2 = defaxis(dataname2, 'CH2')
    
    plt.figure(figsize=(12,8), dpi=100)
    plt.plot(X,Y1,color='y',label='CH1')
    plt.plot(X,Y2,color='b',label='CH2')
    plt.xlabel('Time')
    plt.ylabel('CH')
    plt.legend()
    
def plotdata_norm(dataname1,dataname2): #faz o plot dos canais sobrepostos e normalizados
    X = defaxis(dataname1,'TIME')
    Y1 = defaxis(dataname1, 'CH1')
    Y1_max = max(Y1)
    Y1_min = min(Y1)
    Y2 = defaxis(dataname2, 'CH2')
    Y2_max = max(Y2)
    Y2_min = min(Y2)
    
    Y1_norm = []
    Y2_norm = []
    
    for el in Y1:
        el_norm1 = (el - Y1_min)/(Y1_max - Y1_min)
        Y1_norm.append(el_norm1)
    for el in Y2:
        el_norm2 = (el - Y2_min)/(Y2_max - Y2_min)
        Y2_norm.append(el_norm2)
        
    plt.figure(figsize=(12,8), dpi=100)
    plt.plot(X,Y1_norm,color='y',label='CH1')
    plt.plot(X,Y2_norm,color='b',label='CH2')
    plt.xlabel('Time')
    plt.ylabel('CH')
    plt.legend()

#--------------- params --------------- dados 30/11/2022

headersize = 13
N_i = 34
N_f = 35
datalist = csvname(N_i,N_f)

for el in datalist:
    [dataset1, dataset2] = datacleaner(el[0], el[1], 13)
    plotdata(dataset1,dataset2)

for el in datalist:
    [dataset1, dataset2] = datacleaner(el[0], el[1], 13)
    plotdata_norm(dataset1,dataset2)