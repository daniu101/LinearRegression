#!/usr/bin/env python
# -*- coding: utf-8 

from LR.database_model import read_data


DIR_DATABASE = "D:/LR_Database.txt"

def forecast_y(x):
    data = read_data(DIR_DATABASE)
    kb = data.split() 
    k = float(kb[0])
    b = float(kb[0])
    return k*x+b

x = 5
print(forecast_y(x))

#     
    