#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     08/04/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

NN=10

def printBoard(board):
    #n=
    final=[]
    for c in range(len(board)):
        lis=['- ']*len(board)
        lis[board[c]]='Q '
        final.append(''.join(lis))
    endStr=''
    for st in range(len(board)*2+4):
        endStr+='#'
    print(endStr)
    for n in final:
        print('#',n,'#')
    print(endStr)
def conflict(state, x):
    c=len(state)
    # recieves lsit of integers
    # if conflict, return True
    #else return False
    for i in range(L):
        if state[i]-x==0:
            return True
    print('FIX ME')

def validSolution(solutionList):
    state=[solutionList[0],]
    #finish method
    #return flag
    print('FIX ME')

def creatPosibleBoards(board):
  #  print(board,'= parent')
    finalList=[]
    child=[]+board
    for n in range(len(board)):
        child=[]+board
        for q in range(n, len(board)-1):
            child[q],child[q+1]=child[q+1],child[q]
            finalList.append(child)
            child=[]+child
    return finalList

def singleSwap(board):
    finalLst=[]
    for n in range(len(board)-2):
        currentL=[]+board
        currentL[n],currentL[n+1]=currentL[n+1],currentL[n]
        finalLst.append(currentL)
    return finalLst
#creates all possible permutations.
#so to get a random permutation, pick a random n in the range (len(finalList)) and use that as the parent

#introduce code

#write code fragment to operate on a list called parent (parent=[1,2,3,4])
#then print all single-swap changes of the parent list

#write code to change a list [1,2,3,4,5] into an integer !!Cast list as string and use .join(). then turn string into integer
def cost(board):
    colsi=0
    for q in range(len(board)):
        queenRow=q
        queenCol=board[q]
        for n in range(q+1,len(board)):
            if board[n]==queenCol:
                colsi+=1
            elif abs(queenCol-board[n])==abs(queenRow-n):
                colsi+=1
    return colsi
from random import *
def main():
    initial=[]
    solution=[]
    for n in range(NN):
        initial.append(n)
    allParents=creatPosibleBoards(initial)
    flag=True
    while flag:
        n=randint(0,len(allParents)-1)
        parent=allParents[n]
        Pcost=cost(parent)
        allParents=singleSwap(parent)
        bestChild=[]
        bestCost=9999999
        for child in allParents:
            ccost=cost(child)
            if ccost<bestCost:
                bestChild=child
                bestCost=ccost
            if ccost==0:
                flag=False
                solution=child
        if bestCost<Pcost:
            parent=bestChild
        else:
            allParents=creatPosibleBoards(initial)
    print(solution)
    printBoard(solution)


    #n=randint(0,len(allParents)-1)
    #parent=allParents[n]
    #print(parent)
    #children=singleSwap(parent)
    #print(children)
        #generate list of one pair swaps of parent
        #calulate attacks of each
        #if less than attacks of parent, that's the new one
   # print(parent)

    #print(parent)
        #while the board is viable


if __name__ == '__main__':
    main()

#generate random permutation of digits 0-(n-1)
#genrate all one pair swaps of parent
#choose configuration with lowest score (fewest attacks). this is the new parent
#if new parent score less than original parent's , go to 2nd step and repeat
#if score is NOT smaller, do a random reset and start over (ie go to step 1)
# TADA