#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     24/04/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
POPSIZE=8
from random import *
def createRandChromosomes():
    #each is 10 long
    chromList=[]
    for p in range(POPSIZE):
        currentChrom=[]
        for n in range(10):
            currentChrom.append(randint(0,1))
        chromList.append(currentChrom)
    return chromList
def sortChroms(chromList):
    chromList.sort(key=sum, reverse=True)

def combine(p1,p2):
    number=randint(0,POPSIZE-1)
    c1,c2=p1[:number]+p2[number:],p2[:number]+p1[number:]
    return c1,c2
def main():
    population=createRandChromosomes()
   # print(population)
    population.sort(key=sum,reverse=True)
    #print(population)
    for n in range(20):
        c1, c2=combine(population[0],population[1])
        c3, c4=combine(population[0],population[2])
        c5, c6=combine(population[0],population[3])
        c7, c8=combine(population[0],population[POPSIZE//2])
        population=[c1,c2,c3,c4,c5,c6,c7,c8]
        sortChroms(population)
    for n in population:
        print(n)

    #create a popultatoin of size POPSIZE
    #sort them so that the one wiht the highest collective value is in position 1
    #and so on and so on
    #done up to here
    #then you combine that one with the four below it (chroms[1],chroms[2],chroms[POP//2]
    #each coupling should produce 2 chldren
    #children replace thier population
    #chrm[5],5,7 not allowed because least fit
    #then process is repeated
    #proceed for 20
    #pass

#each has 10 chrom, 100 chromosomes?
#find sum of all 100
#then find the max?

if __name__ == '__main__':
    main()
