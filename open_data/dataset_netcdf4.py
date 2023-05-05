import netCDF4 as nc
import numpy as np
import pandas as pd

class dataset_netcdf4:
    def __init__(self, nc_dimension, nc_dimension_size,path):
        self.nc_ds = nc.Dataset(path,mode='w',format='NETCDF4',encoding='utf-8')
        self.nc_dimension = nc_dimension
        self.nc_dimension_size = nc_dimension_size
        self.createdimensions()
        
    def createdimensions(self):
        for i in range(len(self.nc_dimension)):
            self.nc_ds.createDimension(self.nc_dimension[i],self.nc_dimension_size[i])

    def get_dimension_by_idx_list(self,dimension_idx):
        dimension = ()
        for i in range(len(dimension_idx)):
            dimension += (self.nc_dimension[dimension_idx[i]],)
        return(dimension)

    def add_var(self,var_name,var_value,dimension_idx=[0,1],n_var=1,type=float):
        if n_var == 1:
            var_dim = self.get_dimension_by_idx_list(dimension_idx)
            self.nc_ds.createVariable(var_name,type,var_dim)[:] = var_value
        else:
            for i in range(n_var):
                var_dim = self.get_dimension_by_idx_list(dimension_idx[i])
                self.nc_ds.createVariable(var_name[i],type,var_dim)[:] = var_value[i]