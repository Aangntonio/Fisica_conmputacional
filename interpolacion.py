# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:19:59 2023

@author: Antonio González
"""
#lptm pongan zoe

import numpy as np
import matplotlib.pyplot as plt 



def neville(xDatos, yDatos, x):
    m = len(xDatos)
    y = yDatos.copy()
    for k in range(1,m):
        y[0:m-k] = ((x - xDatos[k:m])*y[0:m-k] +      \
                    (xDatos[0:m-k] - x)*y[1:m-k+1])/  \
                    (xDatos[0:m-k] - xDatos[k:m])
    return y[0]