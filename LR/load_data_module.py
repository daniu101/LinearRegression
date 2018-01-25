#!/usr/bin/env python
# -*- coding: utf-8 

from builtins import int

#导入数据
x = []
y = []

def load_data():
    #数据路径用户根据自己存放位置更改
    for line in open("D:/LR.txt"):  
        line_tmp = line.split()
        _x = int(line_tmp[0])
        _y = int(line_tmp[1])
        
        x.append(_x)
        y.append(_y) 
    
    return x,y