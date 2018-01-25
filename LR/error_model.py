#!/usr/bin/env python
# -*- coding: utf-8 

from LR.lr_model import function

def error(p,x,y,s):
    print (s)
    return function(p,x)-y