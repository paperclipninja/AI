#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     01/05/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#create neural network to serve as an or gate
#x0 is -1
#need 3 inputs and 3 weights
from random import random
from math import *
def ANN_Training(x=[[-1,1,1,0,],[-1,1,0,1],[-1,0,1,1],[-1,0,0,0,]],w0=random()*3-2,w1=random()*3-2,w2=random()*3-2,alpha=.25):
    error=float('inf')
    count=0
    error
    while count<1000:
        for n in range(4):
            dotProd=w0*x[n][0]+w1*x[n][1]+w2*x[n][2]
            t=x[n][3]
            y=1/(1+exp(-dotProd))
            #if dotProd >0:
            #    y=1
            #else: y=0
            error=(t-y)

            w0=w0+alpha*error*x[n][0]
            w1=w1+alpha*error*x[n][1]
            w2=w2+alpha*error*x[n][2]
        count+=1
    return w0,w1,w2
#----------------------------------------------
def ANN(x0,x1,x2,w0,w1,w2):
##    print((x1*w1+x2*w2+w0*x0))
    if x1*w1+x2*w2+w0*x0>0:
        return 1
    else:
        return 0
   # print('solution: ',w0*x0+w1*x1,' w0*x0 ',w0*x0,'x1*w1',x1*w1)

def main():
    w0,w1,w2=ANN_Training()
    print('w0= ',-round(w0,15),'\nw1= ',round(w1,15), '\nw2= ',round(w2,15),sep='')
    print(bool(ANN(-1,1,1,w0,w1,w2)))
    print(bool(ANN(-1,0,1,w0,w1,w2)))
    print(bool(ANN(-1,1,0,w0,w1,w2)))
    print(bool(ANN(-1,0,0,w0,w1,w2)))


    pass

if __name__ == '__main__':
    main()
