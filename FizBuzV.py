#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     04/01/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def inputString():
    print('idk')
    return('abcdefghabc')
def maxMinAvg(diCt):
    minimum=10000
    maximum=0
    avg=0
    for letter in diCt.keys():
        if diCt[letter]<minimum:
            minimum=diCt[letter]
        if diCt[letter]>maximum:
            maximum=diCt[letter]
        avg+=diCt[letter]
    return minimum,maximum, avg/len(diCt.keys())
def sortFreq(diCt):
    d={}
    keyList=([diCt[letter], letter] for letter in diCt.keys())
    keyList=sorted(keyList)
    n=0
    for number in keyList:
            print('%4d\t%4d\t%4d\t'%(ord(number[1]), number[0],),number[1], sep='        ')
            n+=1

def printFrequencyTable(stng, sortByFrequency=0):
    def createDict(stng,sortByFrequency=0):
        numChar=0
        if stng=='':
            print("ERROR: BAD INPUT(null string was encountered")
            return('X')
        if len(stng)>=1000:
            print(" characters. Formatting may be affected")
        diCt={}
        for n in range(len(stng)):
            s=stng[n:n+1]
            if s not in diCt.keys():
                diCt[s]=1
                numChar+=1
            else:
                diCt[s]+=1
        print('')
        printFunctions(diCt,numChar)
        printTable(diCt)
        printOptions()
    def printFunctions(diCt,numChar):
        minimum,maximum, avg=maxMinAvg(diCt)
        print('1. String (first 20 characters):', stng[:20])
        print("2. Lenght of the input string:", len(stng))
        print("3. Nubmer of distinct Chacters:", numChar)
        print("4. Highest frequency=", maximum)
        print('5. lowest frequency=',minimum)
        print('6. average frequency=','%10.2f'%avg)
        print("7. Nubmer of distinct Chacters:", numChar)

    def printTable(diCt):
        print('NUMBER   Unicode  Frequency  Character')
        n=1
        p=[]
        if sortByFrequency=='F':
            sortFreq(diCt)
        else:
            if sortByFrequency=='A':
                p= sorted(diCt.keys())
            else:
                p=diCt.keys()
            for letter in p:
                print('%4d\t%4d\t%4d\t'%(n, ord(letter), diCt[letter]),letter, sep='        ')
                n+=1
        print('-----------------END OF TABLE---------------------------------------')
    def printOptions():
        print("OPTIONS (for the printFrequencyTable function):")
        print('0. print frequencyTable(stng): list in order of occurrence in the string')
        print('1. print frequencyTable(stng,"A"): List in dictionary order')
        print('2. print frequencyTable(stng,"F"): List in order of frequency')
    createDict(stng, sortByFrequency)
def main():
    #stng=inputString()
    printFrequencyTable('ABCDABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHJIKLMS',"A")

if __name__ == '__main__':
    main()
