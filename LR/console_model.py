#!/usr/bin/env python
# -*- coding: utf-8 

import numpy as np
from scipy.optimize import leastsq
from LR.load_data_module import load_data
from LR.error_model import error
from LR.matplotlib_model import matplotlib_show
from LR.database_model import write_data

x,y = load_data()
Xi=np.array(x)
Yi=np.array(y)

p0=[100,2]

s="迭代！" 

DIR = "D:/LR_Database.txt"
Para=leastsq(error,p0,args=(Xi,Yi,s)) 
k,b=Para[0]

matplotlib_show(Xi,Yi,k,b,x)

db_data = "k="+ str(k) + '\n'+"b="+str(b)
write_data(DIR,db_data)

print (db_data)



