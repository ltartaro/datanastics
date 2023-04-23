#IMportar as bibliotecas
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import time
from datetime import datetime
from datetime import timedelta
import matplotlib.dates as mdates
from scipy import stats as st

class AnaliseExploratoria():
  
    
    def __init__(self):
        return None
        
    

    def importarDados(nomeDoArquivo): #str(IAG_Cientec_Tmed_Precip diaria.xlsx)
        dataset = pd.read_excel('/content/drive/MyDrive/AULAS 2023 1º SEMESTRE/Prática Climato II/Prática 1/Dados/'+nomeDoArquivo)
        return dataset

    def inspecaoVisual(dataset,ColunaDaVariavel,tituloDoGrafico,Unidade,colorbar): #'TempMedia_oC';'Temperatura Média Diária (ºC)'
        grossura = 1
        asp = 'go--'
        font1 = {'family':'serif','color':'black','size':20}
        font2 = {'family':'serif','color':'darkred','size':15}
        x =  pd.to_datetime(dataset['Dia'])
        dias = dataset['Dia']

        figure, ax = plt.subplots(figsize=(15, 9))
        ax.set_title(tituloDoGrafico)

        ax.plot(dias,dataset[ColunaDaVariavel],colorbar,linewidth=grossura)
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=60))
        ax.set_xlabel('Dias',fontdict = font1)
        ax.set_ylabel(Unidade,fontdict = font1)

        ax.legend(fontsize=5)
        return plt.show()

    def media(dataset):
        return np.mean(dataset)

    def mediana(dataset):
        return np.median(dataset)

    def desvioPadrao(dataset):
        return np.std(dataset)

    def variancia(dataset):
        return np.var(dataset)

    def moda(dataset):
        return st.mode(dataset)

    def coefAssimetria(dataset):
        return dataset.skew()

    def amplitude(cachorrinho):
        return np.max(cachorrinho)-np.min(cachorrinho)
    

    def histogramaPercentual(dataset,ColunaDaVariavel,tituloDoGrafico,bins,cor,unidade):
        font1 = {'family':'serif','color':'black','size':20}
        colunas = [ColunaDaVariavel]
        H = pd.DataFrame(columns=colunas)
        H[ColunaDaVariavel] = dataset[ColunaDaVariavel]

        #fig, ax = plt.subplots(figsize=(16, 10))
        ax = H.plot.hist(bins=bins, alpha=0.4, grid=True, figsize=(8,10), 
                         layout=(3,1), sharex=True, zorder=2, 
                         rwidth=0.9, color = cor, weights=np.ones(len(dataset))/len(dataset))
        ax.set_xlabel(unidade,fontdict = font1)
        ax.set_ylabel('Frequência',fontdict = font1)
        plt.title(tituloDoGrafico)
        return plt.show()

    def histograma(dataset,ColunaDaVariavel,tituloDoGrafico,bins,cor,unidade):
        font1 = {'family':'serif','color':'black','size':20}
        colunas = [ColunaDaVariavel]
        H = pd.DataFrame(columns=colunas)
        H[ColunaDaVariavel] = dataset[ColunaDaVariavel]

        #fig, ax = plt.subplots(figsize=(16, 10))
        ax = H.plot.hist(bins=bins, alpha=0.4, grid=True, figsize=(8,10), 
                         layout=(3,1), sharex=True, zorder=2, 
                         rwidth=0.9, color = cor, weights=np.ones(len(dataset)))
        ax.set_xlabel(unidade,fontdict = font1)
        ax.set_ylabel('Frequência',fontdict = font1)
        for rect in ax.patches:
          height = rect.get_height()
          ax.annotate(f'{int(height)}', xy=(rect.get_x()+rect.get_width()/2, height), 
                        xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
        plt.title(tituloDoGrafico)
        return plt.show()

    def histogramaLog(dataset,ColunaDaVariavel,tituloDoGrafico,bins,cor,unidade):
        font1 = {'family':'serif','color':'black','size':20}
        colunas = [ColunaDaVariavel]
        dataset = dataset[dataset[ColunaDaVariavel] != 0]
        H = pd.DataFrame(columns=colunas)
        H[ColunaDaVariavel] = np.log(dataset[ColunaDaVariavel])

        #fig, ax = plt.subplots(figsize=(16, 10))
        ax = H.plot.hist(bins=bins, alpha=0.4, grid=True, figsize=(8,10), 
                         layout=(3,1), sharex=True, zorder=2, 
                         rwidth=0.9, color = cor, weights=np.ones(len(dataset)))
        ax.set_xlabel(unidade,fontdict = font1)
        ax.set_ylabel('Frequência',fontdict = font1)
        for rect in ax.patches:
          height = rect.get_height()
          ax.annotate(f'{int(height)}', xy=(rect.get_x()+rect.get_width()/2, height), 
                        xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
        plt.title(tituloDoGrafico)
        return plt.show()

    def histogramaHeterogeneo(dataset,ColunaDaVariavel,tituloDoGrafico,cor,unidade):
        DF = dataset[dataset[ColunaDaVariavel] != 0]
        font1 = {'family':'serif','color':'black','size':20}

        lista = [0,0.3,0.5,0.7,1,2,4,7,15,40,100,180]
        A = []
        for i in range(len(lista)-1):
          a = DF[(DF[ColunaDaVariavel] > lista[i]) & (DF[ColunaDaVariavel] <= lista[i+1])]
          A.append(a)

        B = [len(A[0]),len(A[1]),len(A[2]),len(A[3]),len(A[4]),len(A[5]),len(A[6]),len(A[7]),len(A[8]),len(A[9]),len(A[10])]
        fig = plt.figure(figsize=(16, 10))
        ax = fig.add_subplot(111)
        ax.bar(range(len(B)), B, color='blue')
        xlabel = ['0.1-0.3','0.3-0.5','0.5-0.7','0.7-1','1-2','2-4','4-7','7-15','15-40','40-100','100-180']
        [0.1,0.3,0.5,0.7,1,2,4,7,15,40,100,180]
        plt.xticks(range(len(B)), xlabel[:])
        ax.grid(color='black', linestyle='-', linewidth=0.1)
        ax.set_xlabel(unidade,fontdict = font1)
        ax.set_ylabel('Frequência',fontdict = font1)

        for rect in ax.patches:
          height = rect.get_height()
          plt.annotate(f'{int(height)}', xy=(rect.get_x()+rect.get_width()/2, height), 
                      xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
        plt.title(tituloDoGrafico)
        return plt.show()

    def boxplot(dataset,ColunaDaVariavel,tituloDoGrafico,unidade):
        name = ColunaDaVariavel
        dataset = dataset[dataset[ColunaDaVariavel] != 0]
        fig = plt.figure(figsize =(10, 7))
        # Set the figure size
        plt.rcParams["figure.figsize"] = [10, 5]
        plt.rcParams["figure.autolayout"] = True

        data = [dataset[name]]

        # Creating axes instance
        ax = fig.add_axes([0, 0, 1, 1])
        ax.yaxis.grid(True) # Hide the horizontal gridlines
        ax.xaxis.grid(False) # Show the vertical gridlines
        # Creating plot
        bp = ax.boxplot(data, showmeans=True)

        fig = plt.title(tituloDoGrafico)

        ax.set_xticklabels([unidade])
        return plt.show()

    def percentil(dataset,ColunaDaVariavel,tituloDoGrafico,unidade):
        p = np.linspace(0,100,6001)

        plt.plot(p,np.percentile(dataset[ColunaDaVariavel],p),'--')
        plt.title(tituloDoGrafico)
        plt.ylabel(unidade)
        plt.xlabel('Frequência')
        return plt.show()

    def mediaMensal(dataset, ColunaDaVariavel):
        return dataset.groupby(pd.PeriodIndex(dataset['Dia'], freq="M"))[ColunaDaVariavel].mean()

    def mediaAnual(dataset):
        return dataset.groupby(pd.PeriodIndex(dataset['Dia'], freq="Y"))[ColunaDaVariavel].mean()





