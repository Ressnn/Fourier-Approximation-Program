# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 08:26:00 2020

@author: Pranav Devarinti
"""
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
# In[]
n = 1000
L = 4
# In[]
def MainFunc(x):
    return 2**x
def AFinderFunc(x,n,L):
    return MainFunc(x)*np.cos((n*np.pi*x)/L)
def BFinderFunc(x,n,L):
    return MainFunc(x)*np.sin((n*np.pi*x)/L)

a_0 = (1/L)*quad(MainFunc,-L,L)[0]
an_list = []
bn_list = []
for i in range(0,n):
    an_list.append((1/L)*quad(AFinderFunc,-L,L,args=(i+1,L),limit=1000)[0])
    bn_list.append((1/L)*quad(BFinderFunc,-L,L,args=(i+1,L),limit=1000)[0])

def FourierEquastion(x,a0,n,L,al,bl):
    total = .5*a0
    for i in range(1,n+1):
        total = total+(al[i-1]*np.cos((i*np.pi*x)/L))+(bl[i-1]*np.sin((i*np.pi*x)/L))
    return total

def GraphFourier(a0,n,L,al,bl,start,stop,step):
    Values = np.arange(start,stop,step)
    FV = []
    for i in Values:
        FV.append(FourierEquastion(i,a0,n,L,al,bl))
    plt.plot(Values,FV)
def GraphFunction(func,start,stop,step):
    Values = np.arange(start,stop,step)
    FV = []
    for i in Values:
        FV.append(MainFunc(i))
    plt.plot(Values,FV)
    
GraphFunction(MainFunc,-L,L,.001)
GraphFourier(a_0,n,L,an_list,bn_list,-L,L,.01)
