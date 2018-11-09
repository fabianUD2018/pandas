# -*- coding: utf-8 -*-
"""
Created on Mon May 21 14:39:05 2018

@author: Estudiantes
"""

import numpy
import matplotlib as mpl

import matplotlib.pyplot as plt
numpy.random.seed(2017)
total_f=[]

for j in range(100000):    
    total=[0]
    
    for i in range (10):
        dado=(numpy.random.randint(0,6)+1 +numpy.random.randint(0,6)+1)
        total.append(total[i]+dado)
    total_f.append(total[-1])
#print(total_f)
plt.hist(total_f, bins=20)
