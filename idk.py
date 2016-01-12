#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     18/02/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from itertools import permutations
from math import *

def permute(Lst,r):
    L=len(Lst)
    assert L>=1 and r>=0
    #if L==2:
    #    return [Lst[0]+Lst[1],Lst[1]+Lst[0]]
    Lst=Lst[:]
    if L==1: return Lst
    d=factorial(L-1)
    #print('r',r,'d',d)
    digit=Lst[r//d]
    Lst.remove(digit)
    return[digit]+permute(Lst,r%d)

def main():
    count=1
    for r in range(24):

     print(count, permute([0,1,2,3],r))
     count=count+1

if __name__ == '__main__':
    main()
