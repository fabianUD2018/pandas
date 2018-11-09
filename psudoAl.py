# -*- coding: utf-8 -*-
"""
Created on Mon May 21 14:16:08 2018

@author: Estudiantes
"""

"""aleatorio se generan a partir de una semilla psudoaleatorio"""

import numpy
import matplotlib as mpl
"""mpl.use ("Agg")"""
import matplotlib.pyplot as plt
numpy.random.seed(2017)
total_f=[]
total=[0]
print(total)
for i in range (10):
    moneda=numpy.random.randint(0,2)
    total.append(total[i]+moneda)
print(total)