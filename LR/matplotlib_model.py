#!/usr/bin/env python
# -*- coding: utf-8 

import matplotlib.pyplot as plt
import numpy as np

def matplotlib_show(Xi,Yi,k,b,x):
    plt.figure(figsize=(8,6))
    plt.scatter(Xi,Yi,color="red",label="Sample Point",linewidth=1) 
    
    x=np.linspace(0,70)
    y=k*x+b
    plt.plot(x,y,color="green",label="Fitting Line",linewidth=2) 
    
    plt.legend()
    plt.show()