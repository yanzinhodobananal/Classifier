# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:57:08 2023

@author: Yan - (ALFA)
"""

import os
import numpy as np
import lvm_read as lvm_read
import matplotlib.pyplot as plt
import pandas as pd
import math
import glob


# arquivos = os.listdir(os.getcwd()+'\\Dados')

#%%
def truncate(number, decimals=3):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor






#%%

f = open("CNN_summary_ST.txt","r")
f = f.read()
f = f.split()
f.sort()

lista = []
for i in range(len(f)):
    if len(f[i]) == 47:
        keyword = f[i][0:35]
    elif len(f[i]) == 46:
        keyword = f[i][0:34]
    for fname in os.listdir(os.getcwd()+'\\Dados'):
        if keyword in fname:
            if fname not in lista and fname[-4:] != '.pkl':
                print(fname, "has the keyword")
                lista.append(fname)
        
#%%
# lista = []

# for i in range(len(f)):
#     keyword = f[i][0:35]
#     if keyword in f[i]:
#         lista.append(f[i])
        
# lista.sort()
        
  
#%%
M_air_v=[]
# i= 0 
# for j in range(len(lista)):
    
#     M_air = lista[j].split("kgph")[0].split("_")[-1]
#     M_air = float(M_air.replace(",","."))
#     M_air_v.append(M_air)
#     m_air_v = np.sort(M_air_v)
#%%

# for filename in lista:
#     lvm = lvm_read.read('.\\Dados\\'+filename)
#     data = lvm[0]['data']
#     data_1_trunc =[truncate(x) for x in data[:,12]]

# lista = []
lista_casos = []
for j in range(len(lista)):
    lista_casos = []
    keyword = lista[j]
    if len(keyword) == 38:
        keyword = keyword[0:34]
    elif len(keyword) == 39:
        keyword = keyword[0:35]
    for k in range (len(f)): 
        if keyword in f[k]:
            lista_casos.append(f[k])
            lvm = lvm_read.read('.\\Dados\\'+ keyword + '.lvm')
            data = lvm[0]['data']
            data_trunc = np.array([truncate(x) for x in data[:,12]])
            data_frame = pd.DataFrame(data)
            data_frame.columns = ["X","P0","P1","P2","P3","P4","Plfe","DPlfe","Mliq","Torque","Tliq","Tgas","Mgas","IGVF"]
            classes = []
            classes = np.full(len(data),-1)
            M_air_v.clear()
            m_air_v = np.array([])
            for ii in range(len(lista_casos)):
                M_air = lista_casos[ii].split("kgph")[0].split("_")[-1] 
                M_air = float(M_air.replace(",","."))
                M_air_v.append(M_air)
                m_air_v = np.sort(M_air_v)
                for kk in range(len(data)):
                    if m_air_v[ii] == data_trunc[kk]:
                        classes[kk]=(float(lista_casos[ii][-1]))
                        print(lista_casos[ii])
                        if kk+1<len(data):
                            classes[kk+1]=(float(lista_casos[ii][-1]))
                        if kk+2<len(data):
                            classes[kk+2]=(float(lista_casos[ii][-1]))
        # print(keyword)
                        
                        
                        
    data_frame["Classificação"] = classes
    if 'ST' in fname:
        if '2stg' in keyword:
            data_frame.to_excel('Outputs\\Surging\\2stg\\'+ keyword + ".xlsx")
        elif '3stg' in keyword:
            data_frame.to_excel('Outputs\\Surging\\3stg\\'+ keyword + ".xlsx")
        elif '4stg' in keyword:
            data_frame.to_excel('Outputs\\Surging\\4stg\\'+ keyword + ".xlsx")
# for i in range(len(f)):
#    if len(f[i]) == 47:
#        keyword = f[i][0:35]
#    elif len(f[i]) == 46:
#        keyword = f[i][0:34]
#        for fname in os.listdir(os.getcwd()+'\\Dados'): 
#            if keyword in fname and fname[-4:]!=".pkl":
#              lvm = lvm_read.read('.\\Dados\\'+ fname)  
#              data = lvm[0]['data']
#              data_trunc = np.array([truncate(x) for x in data[:,12]])
#              data_frame= pd.DataFrame(data)

#              classes = []
#              classes = np.full(len(data),-1)
#              M_air_v.clear()
#              m_air_v = np.array([])
#              for j in range(len(lista)):

#                  M_air = f[i].split("kgph")[0].split("_")[-1]
#                  M_air = float(M_air.replace(",","."))
#                  M_air_v.append(M_air)
#                  m_air_v = np.sort(M_air_v)
#                  for k in range(len(data)):
#                      if m_air_v[j] == data_trunc[k]:
#                         classes[k]=(float(f[i][-1]))
#                         classes[k+1]=(float(f[i][-1]))
#                         classes[k+2]=(float(f[i][-1]))

# print(m_air_v)





    # classes = []
    # classes = np.full(len(data),-1)
 
                
            
# classes[(classes>0)&(classes<1)] = 5

    # data_frame["Classificação"] = classes
    # data_frame.to_excel(keyword + ".xlsx")
