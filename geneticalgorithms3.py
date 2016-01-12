#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     18/05/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
POP=1000
from random import *
def createRandChromosomes():
    #each is 10 long
    chromList=[]
    for p in range(POP):
        currentChrom=""
        for n in range(20):
            currentChrom+=str(randint(0,1))
        chromList.append(currentChrom)
    return chromList
def seperateXandY(chrom):
    x=y=""
   # print("chrom=",chrom)
    x=chrom[:10]
    y=chrom[10:]
    x=int(x,2)
    y=int(y,2)
    return x/102,y/102
    #divide by 102
def sortChroms(chromList):
    chromList.sort(key=findFitness, reverse=True)
    return chromList
from math import *
def findFitness(chrom):
    x,y=seperateXandY(chrom)
    fit=x*sin(4*x)+1.1*y*sin(2*y)
    return fit
    #print("NOT WOKRING")
def combine(p1,p2):
    number=randint(0,POP-1)
    c1,c2=p1[:number]+p2[number:],p2[:number]+p1[number:]
    return c1,c2

def main():
    chroms=createRandChromosomes()
    for n in range(100):
        chroms=sortChroms(chroms)
        p1=chroms[0]
        p2=chroms[1]
        p3=chroms[2]
        p4=chroms[3]
        chroms[POP-1],chroms[POP-2]=combine(p1,p2)
        chroms[POP-3],chroms[POP-4]=combine(p1,p3)
        chroms[POP-5],chroms[POP-6]=combine(p1,p4)

    #repeat 20 times
    x,y=seperateXandY(chroms[0])
    print("x",x)
    print("y", y)
if __name__ == '__main__':
    main()
