# -*- coding: utf-8 -*-
from open_data import*
from open_data.importations import *
from open_data.dataset_netcdf4 import *
from open_data.open_data import *

importations()

path = r"C:\Users\Lucas\Documents\dados_lipe"
name_ncfile = r'\nc_meteo_data.nc'

dados_brutos = open_data(file_path=path).DATA

nc_dimension = ['day','hour']
nc_dimension_size = np.shape(np.array(dados_brutos)[0,:,:12])
dado_netcdf4 = dataset_netcdf4(nc_dimension, nc_dimension_size,path+name_ncfile)

#Solução pois a coluna também era dimensão
dado_netcdf4.add_var('days',np.array(dados_brutos[0].iloc[:,12]),
                     [0],n_var=1,type=str)

#Solução pois não foi importado dado com horário
dado_netcdf4.add_var('hours',np.arange(12,24),
                     [1],n_var=1,type=int)

#Solução do programa para dados maiores
var_names = ['q500','t500','u500','UR500','v500']
var_dim=[[0,1],[0,1],[0,1],[0,1],[0,1]]
dado_netcdf4.add_var(var_names,np.array(dados_brutos)[:,:,:12],
                     var_dim,n_var=np.shape(var_names)[0],type=float)

print(dado_netcdf4.nc_ds,'ex_dado',dado_netcdf4.nc_ds['q500'][:])