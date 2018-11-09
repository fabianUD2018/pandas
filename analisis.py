# -*- coding: utf-8 -*-
"""
Created on Wed May 23 23:00:51 2018

@author: fcher
"""
import pandas as pd
import matplotlib as mpl

import matplotlib.pyplot as plt
datos = pd.read_csv("emb.csv")
#print (datos.head(5))
datosRel= datos[[ 'SEXO', 'PESO_NAC', 'TALLA_NAC', 'ANO' ,'MES' ,'T_GES' ,'TIPO_PARTO','EDAD_MADRE','EST_CIVM','NIV_EDUM','ULTCURMAD','N_HIJOSV','N_EMB','EDAD_PADRE','NIV_EDUP','ULTCURPAD']]

print(datosRel.info())

print("----------------------")

##filtrado de datos atipicos
datosFilt= datosRel[datosRel['NIV_EDUP']< 99  ]
datosFilt= datosFilt[datosFilt['ULTCURPAD']< 99  ]
datosFilt= datosFilt[datosFilt['NIV_EDUM']<99  ]
datosFilt= datosFilt[datosFilt['T_GES']<99  ]
datosFilt= datosFilt[datosFilt['ULTCURMAD']<99  ]
datosFilt= datosFilt[datosFilt['PESO_NAC']<9999  ]
datosFilt= datosFilt[datosFilt['EDAD_PADRE']<99 ]
datosFilt= datosFilt[datosFilt['TALLA_NAC']<99 ]

print(datosFilt.info())
print(datosFilt.describe())

print (datosFilt.corr())
fig=plt.gcf()

datosFilt.plot.scatter('EDAD_MADRE', 'EDAD_PADRE')
datosFilt.plot.scatter('EDAD_MADRE', 'PESO_NAC')
datosFilt.plot.scatter('EDAD_MADRE', 'TALLA_NAC')
datosFilt.plot.scatter('EDAD_MADRE', 'T_GES')
datosFilt.plot.scatter('EDAD_MADRE', 'N_EMB')
datosFilt.plot.scatter('NIV_EDUM', 'N_EMB')
datosFilt.plot.scatter('NIV_EDUM', 'N_HIJOSV')

datosFilt.hist('NIV_EDUM')
datosFilt.hist('EDAD_MADRE')

datosFilt.hist('EDAD_PADRE')
datosFilt.hist('NIV_EDUP')

#datos.hist['NOM_INST'].to_string()
raw_input("Pulsa una tecla para continuar...") 

