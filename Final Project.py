# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:45:40 2017
@author: jonfr
"""
from  scipy import *
from  pylab import *
import math 
import numpy as np
import scipy.misc as sm
np.set_printoptions(threshold=1000)

def Converttoarray(x):
    array=sm.imread(x , True)
    if array.shape[0]%2==1:
        array=array[:-1,:]
        if array.shape[1]%2==1:
            array=array[:,:-1]
    elif array.shape[1]%2==1:
        array=array[:,:-1]
    return array

def HaarWavelet(array):
    haararray=np.zeros((array.shape[0],array.shape[0]))
    for i in range(haararray.shape[0]):
        haararray[int(i/2),i]=1/2
        haararray[-int(i/2)-1,-i-1]=-1/2
    b=dot(haararray,array)
    sm.imsave('AAA.jpg', b)
    haararray=np.zeros((array.shape[1],array.shape[1]))
    for i in range(haararray.shape[1]):
        haararray[int(i/2),i]=1/2
        haararray[-int(i/2)-1,-i-1]=-1/2
    t=np.transpose(2*haararray)
    e=dot(b,t)
    sm.imsave('AAB.jpg',e)
    
HaarWavelet(Converttoarray('kvinna.jpg'))

