#Baixar xarray

#Logica interessante pra juntar os arquivos de Pandas:
#O pandas le o arquivo excel q tem varias paginas, que se chama
#pd.ExcelFile(). Nele entramos com o sheet que interessa para acessarmos a tabela de interesse.
#Exemplo:
#excel = pd.ExcelFile('C:\Users\uli\Documents\USP\entos\Macrofauna_Ubatuba_Disciplina_Bentos_2021.xlsx')
#fauna = excel.parse(sheet_name=excel.sheet_names[0])
#Criar variaveis especificas para cada tipo de dado tambem para poder criar apends especificos.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr
#import xarray as xr

#Todas essas bibliotecas servem pra pegar o dado
import os
import glob
from os.path import basename
from os.path import abspath
from os.path import join

#all_data_path pode receber valores como True, False, 'names', 'any'

class open_data:
    def __init__(self,file_path=[],files=[],all_data_path=True,data_type='txt'):
        self.data = []
        self.file_path = file_path
        self.data_type = data_type
        self.all_data_path = all_data_path #se falso, deve especificar o arquivo
        self.proxy_path = False #caso o arquivo esteja em outro diretorio
        self.any_word = [] #qualquer seq de letras para busca de dados na pasta desejada
        self.files = files #Pode configurar direto pelo utlizador
        self.data_path =self.search_data_path()
        self.data = self.load_data_path()
    
    #Funcao utilizada caso queira procurar dados pelo nome do arquivo
    def name_data_path(self):
        if (self.files == []):
            print('Insira os nome dos arquivos desejados no formato:')
            print("Arquivo_1.tipo,Arquivo_2.tipo,Arquivo_3.tipo")
            file_named = (input('\n'))
            file_named = file_named.split(',')
            self.files = file_named
    
    #instalar dados descompactados na pasta dados
    #Funcao busca dados. Ela pode trabalhar de duas formas:
    #1- Ela busca todos os dados do tipo self.data_type instalados dentro
    #da pasta dados
    #2- Ela busca as pastas pelo nome, utilizando a funcao name_data_path
    def search_data_path(self):
        path = self.file_path
        if self.proxy_path == True: #caso o dado nao esteja na pasta data
            path = os.getcwd()
            path = join(path,'Data')
        elif self.all_data_path == True:
            self.files_names = glob.glob(path+'/*.'+self.data_type)
            self.files_names.sort()
            print(path,self.files_names)
            return(self.files_names)
        elif (self.all_data_path == 'names'):
            files_names = self.files
            if self.files == []:
                print("Utilize o comando name_data_path para nomear os arquivos desejados")
            else:
                for i in range(len(files_names)):
                    files_names[i] = path+'\\'+files_names[i]
                    print(path,self.files_names)
                return(self.files_names)
            return(self.files_names)
        elif (self.all_data_path == 'any'):
            self.data_path = []
            self.files_names = []
            if self.any_word == []:
                self.any_word = input('Digite a sequencia de letras que deseja buscar \n')
            all_names = glob.glob(path+'/*')
            print('Todas as pastas sao:\n',all_names)
            print('Sua pasta possui',len(all_names),'dados.')
            for k in all_names:
                if (self.any_word in k) == True:
                    self.files_names.append(k)
            print('As pastas selecionadas foram:',self.files_names)
            self.data_path = self.files_names
            return(self.files_names)
        elif self.all_data_path == False:
            return ([])

    def load_data_path(self):
        self.DATA = [] # vai ser um vetor cheio de matrizes dentro
        dat = np.array([0])
        k = 0
        for i in self.data_path:
            if '.txt'   in i:
                try:
                    print('Arquivo encontrado')
                    print(self.DATA)
                    dat = pd.read_csv(i,delimiter = " ")
                except:
                    print('Arquivo não encontrado')
                self.DATA.append(dat)
            elif '.csv' in i:
                try:
                    print('Arquivo encontrado')
                    print(self.DATA)
                    dat = pd.read_csv(i,delimiter = ",")
                except:
                    print('Arquivo não encontrado')
                self.DATA = dat
            elif '.xlsx' in i:
                try:
                    print('Arquivo encontrado')
                    print(self.DATA)
                    dat = pd.read_excel(i)
                except:
                    print('Arquivo não encontrado')
                self.DATA = dat
            elif '.mat' in i:
                return()
            elif '.bin' in i:
                return()
            elif '.nc'  in i:
                return()
            k += 1
        self.data = self.DATA
