# -*- coding: utf-8 -*-
"""
Created on Mon May 21 14:56:18 2018

@author: Estudiantes
"""

import pandas as pd
import matplotlib as mpl

import matplotlib.pyplot as plt
datos = pd.read_csv("sabe11.csv")
print (datos.head(50))
print(datos.describe())
datosResumidos=datos[['ESTU_EDAD',  'ESTU_GENERO', 'PUNT_C_NATURALES', 'PUNT_SOCIALES_CIUDADANAS', 'PUNT_INGLES' ,'PUNT_GLOBAL' ]]
print (datosResumidos.corr())
fig=plt.gcf()
datosResumidos.plot.scatter('ESTU_EDAD', 'PUNT_GLOBAL')
fig.savefig("output.png")
datosResumidos.plot.scatter('PUNT_C_NATURALES', 'PUNT_INGLES' )
#cajas y bigotes trabajr cuartiles y la media
datosResumidos.boxplot('PUNT_GLOBAL')

datosResumidos.boxplot('ESTU_EDAD')
datosResumidos.plot('ESTU_EDAD', 'PUNT_GLOBAL')
datosResumidos.hist('ESTU_EDAD')
fig.savefig("histEdades.png")
