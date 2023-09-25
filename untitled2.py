# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:53:06 2023

@author: Antonio González
"""

import numpy as np
import matplotlib.pyplot as plt 

from interpolacion import neville
x0 = np.array([4.0, 3.9, 3.8, 3.7])
y0 = np.array([-0.06604, -0.02724, 0.01282, 0.05382])

x = neville(y0,x0,0)

plt.plot(x0, y0, 'b+')
plt.plot(x0, y0, 'r--', lw=0.6)
plt.plot(x, 0, 'ro')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Gráfica de interpolación con la técnica de Neville')
plt.axhline(y=0, lw=0.7, ls='dashed', color='k')
plt.text(3.85, 0.01, 'y(' + str(round(x,3)) + ') = 0')
plt.show()
