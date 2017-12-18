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
        haararray[int(i/2),i]=(2**(1/2))/2
        haararray[-int(i/2)-1,-i-1]=-(2**(1/2))/2
    for i in range(haararray.shape[0]//2):
        haararray[-i-1,-2*i-1]=(2**(1/2))/2
    b=dot(haararray,array)
    sm.imsave('AAA.jpg', b)
    haararray1=np.zeros((array.shape[1],array.shape[1]))
    for i in range(haararray1.shape[1]):
        haararray1[int(i/2),i]=(2**(1/2))/2
        haararray1[-int(i/2)-1,-i-1]=-(2**(1/2))/2
    for i in range(haararray1.shape[1]//2):
        haararray1[-i-1,-2*i-1]=(2**(1/2))/2
    t=np.transpose(haararray1)
    e=dot(b,t)
    sm.imsave('AAB.jpg',e)
    aa=e[:int(e.shape[0]/2),:int(e.shape[1]/2)]
    sm.imsave('aa.jpg',aa)
    ab=e[:int(e.shape[0]/2),int(e.shape[1]/2):]
    sm.imsave('ab.jpg',ab)
    ac=e[int(e.shape[0]/2):,:int(e.shape[1]/2)] 
    sm.imsave('ac.jpg',ac)
    ad=e[int(e.shape[0]/2):,int(e.shape[1]/2):]  
    sm.imsave('ad.jpg',ad)
    m=column_stack((aa,ab))
    n=column_stack((ac,ad))
    mn=vstack((m,n))
    return mn
    
def Revert(array):
    haararray=np.zeros((array.shape[0],array.shape[0]))
    for i in range(haararray.shape[0]):
        haararray[int(i/2),i]=(2**(1/2))/2
        haararray[-int(i/2)-1,-i-1]=-(2**(1/2))/2
    for i in range(haararray.shape[0]//2):
        haararray[-i-1,-2*i-1]=(2**(1/2))/2
    haararray1=np.zeros((array.shape[1],array.shape[1]))
    for i in range(haararray1.shape[1]):
        haararray1[int(i/2),i]=(2**(1/2))/2
        haararray1[-int(i/2)-1,-i-1]=-(2**(1/2))/2
    for i in range(haararray1.shape[1]//2):
        haararray1[-i-1,-2*i-1]=(2**(1/2))/2
    f=dot(np.transpose(haararray),dot(array,haararray1))
    sm.imsave('AAC.jpg',f)
    return print('hi')



def HaarIterate(array,t=1):
    for i in range(t):
        HaarWavelet(array)
        array=Converttoarray('aa.jpg')
    ab=Converttoarray('ab.jpg')
    ac=Converttoarray('ac.jpg')
    ad=Converttoarray('ad.jpg')
    m=column_stack((array,ab))
    n=column_stack((ac,ad))
    mn=vstack((m,n))
    return mn


Revert(HaarIterate(Converttoarray('kvinna.jpg'),3))

