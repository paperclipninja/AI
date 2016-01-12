#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Arianna
#
# Created:     05/05/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
POPSIZE=10
from random import *
def createRandChromosome():
    #each is 10 long
    chromList=[]
    for p in range(POPSIZE):
        currentChrom=[]
        for n in range(10):
            currentChrom.append(randint(0,1))
        chromList.append(currentChrom)
    return chromList
def sortChroms(chromList):
    chromList.sort(key=fitness, reverse=True)
def combine(p1,p2):
    creature1=[]
    creature2=[]
    #print("p1 ",p1," P2 ",p2)
    for n in range(10):
        #print("N ",n)
        #print("p1 n",p1[n], "p2 n ",p2[n])
        c1,c2=combinechrom(p1[n],p2[n])
        creature1.append(c1)
        creature2.append(c2)
    return creature1,creature2
def combinechrom(p1,p2):
    number=randint(0,POPSIZE-1)
    c1,c2=p1[:number]+p2[number:],p2[:number]+p1[number:]
    return c1,c2
def fitness(creature):
    total=0
    for n in creature:
        total+=sum(n)
    return total
def main():
    population=[]
    for n in range(10):
        population.append(createRandChromosome())
    population.sort(key=fitness,reverse=True)
   # print(population)
    print("INITIAL SORT")
    for n in population:
        print(fitness(n))

    for n in range(120):
        c1, c2=combine(population[0],population[1])
        c3, c4=combine(population[0],population[2])
        c5, c6=combine(population[0],population[3])
        c7, c8=combine(population[0],population[POPSIZE//2])
        population[2]=c1
        population[3]=c2
        population[4]=c3
        population[5]=c4
        population[6]=c5
        population[7]=c6
        population[8]=c7
        population[9]=c8
       # print("-----------------GOT TO THIS POINT-------------------------------")
        population.sort(key=fitness,reverse=True)
    print("FINAL FITNESS VALUES")
    for n in population:
        print(fitness(n))
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

