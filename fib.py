#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     28/10/2013
# Copyright:   (c) Arianna 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from time import clock
def fib1(n):
    a=1;
    b=1;
    for q in range(n-2):
        c=a+b
        a=b
        b=c
    return b
def fib2(n):
    if n<3:
        return 1
    else:
        return fib2(n-1)+fib2(n-2)
def fib3(n):
    if n<3: return 1
    a=1;b=1;
    for i in range(n-2):
        a, b = b , a+b
    return b
def fib4(n):
    if n<3: return 1
    if n==3: return 2
    if n==4: return 3
    if n==5: return 5
    if n==6: return 8
    else:
        return fib4(n-1)+fib4(n-2)
def fib5(n):
    return[0,1,1,2,3,5,8,13,21,34,44,89,144][n]
def fib6(n,D):
    if n in D:
        return D[n]
    D[n]= fib6(n-1,D)+fib6(n-2,D)
    return D[n]
def fib7(n):
    from math import sqrt
    a=(1+sqrt(5))/2
    b=(1-sqrt(5))/2
    return int((a**n-b**n)/sqrt(5))


def main():
    n=36
   # print('fib2(',n ,')=',fib2(36))
   # print('fib3(',n ,')=',fib3(n))
   # print('fib4(',n ,')=',fib4(n))
  #  print('fib5(',n ,')=',fib5(n))
  #  print('fib6(',n ,')=',fib6(n,{1:1,2:1}))
  #  print('fib7(',n ,')=',fib7(n))
  #  print('fib3(',n ,')=',fib3(n))
    printEt()
def printEt():
    print('\n---Total time=',round(clock()-start,2),'seconds.')


if __name__ == '__main__':start=clock(); main()
