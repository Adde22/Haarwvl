# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 13:16:18 2017

@author: jim_k
"""

from scipy import *
import scipy.misc as sm
from numpy import *

img=sm.imread('kvinna.jpg',True)    #Load image into python as array

#Check, slice img array to fit the confience of program
if img.shape[0]%2!=0 or img.shape[1]%2!=0:   #Divide by 2 check remainder
    if img.shape[0]%2!=0:
        img=img[:-1]     #Slice last row
    if img.shape[1]%2!=0:
        img=img[:,:-1]   #Slice last column

#Matrix construct
#WM-matrix which will be multiplyed from the left
WM=zeros((img.shape[0],img.shape[0]))   #Array with zeros shape number of rows
for n in range(img.shape[0]//2):    #Filling array with sqrt(2)/2
#First half of array
    WM[n,2*n]=sqrt(2)/2                 #Each row and row times 2
    WM[n,2*n+1]=sqrt(2)/2               #Each row and row times 2 + 1
#Secong half of array
    WM[int(img.shape[0]/2)+n,2*n]=-sqrt(2)/2    #As previous only nalf way down
    WM[int(img.shape[0]/2)+n,2*n+1]=sqrt(2)/2

#WNT-matrix, multiplyed from the right
WNT=zeros((img.shape[1],img.shape[1]))  #Zero martix with shape of columns
for n in range(int(img.shape[1]/2)):
#First half of array
    WNT[n,2*n]=sqrt(2)/2        #Same method as above
    WNT[n,2*n+1]=sqrt(2)/2
    WNT[int(img.shape[1]/2)+n,2*n]=-sqrt(2)/2
    WNT[int(img.shape[1]/2)+n,2*n+1]=sqrt(2)/2
WNT=WNT.transpose()     #Matrix transpose in order for the effect to be latheral

#Temp img comp
imgdata=dot(WM,dot(img,WNT))

#Save function
sm.imsave('imgcomp.jpg',imgdata)

#Sub-array dividing
aa=imgdata[:int(imgdata.shape[0]/2),:int(imgdata.shape[1]/2)]   #Top left
sm.imsave('aa.jpg',aa)

ad=imgdata[:int(imgdata.shape[0]/2),int(imgdata.shape[1]/2):]   #Top right
sm.imsave('ad.jpg',ad)

da=imgdata[int(imgdata.shape[0]/2):,:int(imgdata.shape[1]/2)]   #Bottom left
sm.imsave('da.jpg',da)

dd=imgdata[int(imgdata.shape[0]/2):,int(imgdata.shape[1]/2):]   #Bottom right
sm.imsave('dd.jpg',dd)

#Reload of subarrays and stacking them.

aa=sm.imread('aa.jpg',True)
da=sm.imread('da.jpg',True)
ad=sm.imread('ad.jpg',True)
dd=sm.imread('dd.jpg',True)

m=column_stack((aa,ad))
n=column_stack((da,dd))
mn=vstack((m,n))

#Apply invers Haar Transformation.

#Invers Haar Transformation function
inversWM=WM.transpose()     #Transpose original Wavelet Matrices for revers transform
inversWNT=WNT.transpose()
inversdata=dot(inversWM,dot(imgdata,inversWNT)) #Appling invers to compress data
sm.imsave('inversimg.jpg',inversdata)       #Save umcompressed data
stackedmn=dot(inversWM,dot(mn,inversWNT))
sm.imsave('wow2.jpg',stackedmn)
#Haar Compression

#Repeating compression and slicing n times

#No Matrix multiplication

#No Matrix multiplication
Non=zeros((img.shape[0],img.shape[1]))
for n in range((img.shape[0])//2-1):
    for m in range((img.shape[1])//2-1):
        Non[n,m]=(img[n*2,m*2]+img[n*2,2*m+1]+img[2*n+1,2*m]+img[2*n+1,2*m+1])/4
        Non[n,img.shape[1]//2+m]=(-(img[2*n,2*m])+img[2*n,2*m+1]-img[2*n+1,2*m]+img[2*n+1,2*m+1])/4
        Non[img.shape[0]//2+n,m]=(-(img[2*n,2*m])-img[2*n,2*m+1]+img[2*n+1,2*m]+img[2*n+1,2*m+1])/4        
        Non[img.shape[0]//2+n,img.shape[1]//2+m]=(-(img[2*n,2*m])+img[2*n,2*m+1]+img[2*n+1,2*m]-img[2*n+1,2*m+1])/4
sm.imsave('Non.jpg',Non)
