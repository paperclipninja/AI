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
def printBoard(board):
    #n=8
    final=[]
    for c in range(len(board)):
        lis=['- ']*len(board)
        lis[board[c]]='Q'
        final.append(''.join(lis))
    print('#######################')
    for n in final:
        print('#',n,'#')
    print('#######################')

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
from copy import*
def parentSwap(board):
    print(board,'= parent')
    finalList=[]
    child=[]+board
    for n in range(len(board)):
        child=[]+board
        for q in range(n, len(board)-1):
            child[q],child[q+1]=child[q+1],child[q]
            finalList.append(child)
            child=[]+child
    for a in finalList:
        print(a)


def main():
    board=[0,1,2,3,4]
    printBoard(board)
    print(cost(board))
    parentSwap(board)

if __name__ == '__main__':
    main()
#If it is at 2,2
#and is checking if one with coordinates 4,4





