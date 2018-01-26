#!/usr/bin/env python
# -*- coding: utf-8 

import numpy as np
from scipy.optimize import leastsq
from LR.load_data_module import load_data
from LR.error_model import error
from LR.matplotlib_model import matplotlib_show
from LR.database_model import write_data

DIR_DATASET = "D:/LR.txt"
DIR_DATABASE = "D:/LR_Database.txt"

p0=[100,2] #存放w、b初始值，可任意制定
x,y = load_data(DIR_DATASET)
Xi=np.array(x)
Yi=np.array(y)
s="迭代！" 

Para=leastsq(error,p0,args=(Xi,Yi,s)) 
k,b=Para[0]

matplotlib_show(Xi,Yi,k,b,x)

db_data = str(k) + ' ' + str(b)
write_data(DIR_DATABASE,db_data)

print ("k="+ str(k) + '\n'+"b="+str(b))



