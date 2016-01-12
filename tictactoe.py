#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     12/06/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from itertools import permutations
def Len(lists):
    return len(lists)-1040
#boardCollection={'--------'=0}
def insertX(board,number):
    #print(board, " ",number)
    board=board[:number]+"X"+board[number+1:]
    return board

def insert0(board,number):
    board=board[:number]+"O"+board[number+1:]
    return board

def isWin(board):
    score={"XXX","OOO"}
    if board[0]+board[1]+board[2] in score or board[3]+board[4]+board[5] in score or\
    board[6]+board[7]+board[8] in score or board[0]+board[3]+board[6] in score or\
    board[1]+board[4]+board[7] in score or board[2]+board[5]+board[8] in score or\
    board[0]+board[4]+board[8] in score or board[2]+board[4]+board[6] in score:
        return True
    return False

def stringBoard(perm,limit):
    newBoard='---------'
    for n in range(limit):
        if n%2==0:
            newBoard=insertX(newBoard,perm.index(n))
        else:
            newBoard=insert0(newBoard,perm.index(n))
    return newBoard

def main():
    permList=list(permutations([0,1,2,3,4,5,6,7,8],9))
    #print(permList[1])
    solutionList={'---------':[9,9,9,9,9,9,9,9,9]}
    #each number = location to put next spot
    #alternate between O and X
    for perm in permList:
        board="---------"
        #print(permList[1])
        for x in range(8):
            subBoard=stringBoard(perm,x)
            if isWin(board):break
            solutionList[subBoard]=perm#solutionList[permList]+=append(board)
    print(Len(solutionList))

if __name__ == '__main__':
    main()
#first come up with a generic permutation thing
#then create all possible variations of that