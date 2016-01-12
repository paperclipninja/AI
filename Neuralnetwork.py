#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     29/04/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import random

def ANN_Training(x0=2,x1=6,w0=4,w1=-2,t=0,alpha=.01):
    error=float('inf')

    count=0
    while abs(error)>0.000000001 and count<3000:
        y=(x0*w0)+(x1*w1)
        error=t-y
        if f(error):
            break
        w0=w0+alpha*error*x0
        w1=w1+alpha*error*x1
        count+=1
        print('Count= ',count,'error= ',error)
    print('y= ',-round(w0/w1,4),'x',sep='')
    return w0,w1
        #calculate error


def f(y): #activation function?
    #if y close to zero, return true
    #else
    if-.000000000000000001<y<.00000000000000000001:
        return 1
    else:
        return 0
    #print("FIX ME")


def ANN(x0,x1,w0,w1):
   # print('solution: ',w0*x0+w1*x1,' w0*x0 ',w0*x0,'x1*w1',x1*w1)
    if abs(w0*x0+w1*x1)<0.000001:
        return True
    else:
        return False
    #print("FIX ME")


def main():
    x0=2;x1=6

    w0,w1= ANN_Training(x0,x1,w0=.5,w1=-.3,t=0,alpha=.001)
    print('w0= ',-round(w0,15),'\nw1= ',round(w1,15),sep='')
    print('y= ',-round(w0/w1, 15),'x',sep='')

    print(ANN(x0,x1,w0 ,w1))
    print(ANN(1000,3000,w0,w1))
    print(ANN(17,51,w0,w1))
    print(ANN(7,8,w0,w1))
    print(ANN(40000,120000+1,w0,w1))
    print(ANN(40000,120000-1,w0,w1))
    print(ANN(40000,120000,w0,w1))
#    print(ANN())

if __name__ == '__main__':
    main()
