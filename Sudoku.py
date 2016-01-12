#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     29/10/2013
# Copyright:   (c) Arianna 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from copy import deepcopy
class Cell(object):
    matrix=None
    def __init__(self,val,r,c,matrix):
        if val==0:
            self.value=set(range(1,MAX+1))
        else:
            self.value={val,}
        self.row=r
        self.col=c
        self.block=self.blockNumber(r,c)
        Cell.matrix=matrix
    def __repr__(self):
        if len(self.value)==1:
            element=str(list(self.value)[0])
        else:
            element=' '
        return element
    def print(matrix, details=False):
        print('+---'*MAX+'+')
        for r in range(MAX):
            for c in range(MAX):
                if len(Cell.matrix[r][c].value)==1:
                    elt=list(Cell.matrix[r][c].value)[0]
                    print('|',elt,' ',end='',sep='')
                else: print('|   ',end='',sep='')
            print('|')
            print('+---'* MAX+ '+')
        print()
        if details==True:
            for r in range(MAX):
                for c in range(MAX):
                    print('matrix[',r,'][',c,'].value=',matrix[r][c].value,sep='')
                print()
    def blockNumber(self,row,col):
        if    (self.row<3) and (self.col<3):   return 0
        if    (self.row<3) and (2<self.col<6): return 1
        if    (self.row<3) and (5<self.col):   return 2
        if  (2<self.row<6) and (  self.col<3): return 3
        if  (2<self.row<6) and (2<self.col<6): return 4
        if  (2<self.row<6) and (5<self.col):   return 5
        if    (5<self.row) and (  self.col<3): return 6
        if    (5<self.row) and (2<self.col<6): return 7
        if    (5<self.row) and (5<self.col):   return 8

    def reduceCellCanditatesByRow(self):
        for r in range(MAX):
            if r!=self.row and len(Cell.matrix[r][self.col].value)==1:
                self.value -= Cell.matrix[r][self.col].value
    def reduceCellCandidatesByCol(self):
          for c in range(MAX):
            if c!=self.col and len(Cell.matrix[self.row][c].value)==1:
                self.value-=Cell.matrix[self.row][c].value

    def reduceCellCandidatesByBlock(self):
        for r in range(MAX):
            for c in range(MAX):
                if(Cell.matrix[r][c].block==self.block) and (r!=self.row or c!=self.col) and len(Cell.matrix[r][c].value)==1:
                    self.value-=Cell.matrix[r][c].value
    def updateCellBasedOnCandidateValuesInItsRowColAndBlock(self):
        rowCandidates=[]
        colCandidates=[]
        blkCandidates=[]
        for c in range(MAX):
            rowCandidates+=Cell.matrix[self.row][c].value
        for r in range(MAX):
            if r!=self.row:
                colCandidates+=Cell.matrix[r][self.col].value
        for r in range(MAX):
            for c in range(MAX):
                if r!=self.row or c!=self.col:
                    if Cell.matrix[r][c].block==self.block:
                        blkCandidates+=Cell.matrix[r][c].value
        for num in self.value:
            if(num not in rowCandidates) or(num not in colCandidates) or (num not in blkCandidates):
                self.value={num,}
    def TryToReduceCandidateValuesInCell(self):
        oldValue=deepcopy(self.value)
        if len(self.value)==1:
            return False
        self.reduceCellCanditatesByRow()
        self.reduceCellCandidatesByCol()
        self.reduceCellCandidatesByBlock()
        self.updateCellBasedOnCandidateValuesInItsRowColAndBlock()
        return self.value!=oldValue
def setUpCanvas(root):
    root.title("SUDOKU: A tk/Phyton Graphics Program by Arianna Sze")
    canvas=Canvas(root,width=1290,height=710,bg='black')
    canvas.pack(expand=YES,fill=BOTH)
    return canvas
def displayTheSudokuBoard(matrix):
   canvas.delete('all')
   canvas.create_rectangle(0,0,1370,710,fill='BLACK')
   canvas.create_rectangle(375,170,735,560,width=4,outline='RED',fill='BLUE')
   kolor='RED'
   for i in range(10):
    canvas.create_line(375+i*40,170,375+i*40,560,fill='RED')
   for q in range(10):
    canvas.create_line(375,170+q*44,735,170+q*44,fill='RED') #560-170/10=390/10=39
   for r in range(MAX):
    for c in range(MAX):
        if len(matrix[r][c].value)!=1:
            ch=' '
        else:
            ch=list(matrix[r][c].value)[0]
        canvas.create_text(c*40+395, r*42+200,text=ch,fill='YELLOW',font=('Helvetica',20,'bold'))
def createTheSudokuBoard():
    V= [[0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [2,0,0,0,0,0,0,0,0,],
        [3,0,0,0,0,0,0,0,0,],
        [0,0,0,3,0,1,0,2,0,],
        [0,0,0,0,2,0,3,0,1,],
        [0,0,0,0,0,0,0,0,0,],]
    matrix=[]
    for r in range(MAX):
        row=[]
        for c in range(MAX):
            row.append(Cell(V[r][c],r,c,matrix))
        matrix.append(row)
    return matrix

def solutionIsCorrect(matrix):
    if matrix==None:
        return False
    rows=[[],[],[],
          [],[],[],
          [],[],[],]
    cols=[[],[],[],
          [],[],[],
          [],[],[],]
    blocks=[[],[],[],
            [],[],[],
            [],[],[],]
    for x in range(MAX):
        for y in range(MAX):
            rows[x].append(Cell.matrix[x][y].value)
            cols[y].append(Cell.matrix[x][y].value)
            blocks[matrix[x][y].block].append(Cell.matrix[x][y].value)

    for r in range(MAX):
        for n in range(1,MAX+1):
             if not {n} in rows[r]:
                return False
             if not{n} in cols[r]:
                return False
             if not{n} in blocks[r]:
                return False
    return True
def coordinatesofCelWithSmallestValuesSet(matrix):
    big=10
    sml=2
    bestRow=-1
    bestCol=-1
    for r in range(MAX):
        for c in range(MAX):
            length=len(matrix[r][c].value)
            if sml<=length<big:
                big=length
                bestRow=r
                bestCol=c
    return(bestRow,bestCol)



def printVerification(matrix):
    if solutionIsCorrect(matrix):
        canvas.create_text(565,600,text="this Sudoku is correct", fill='WHITE',font=('Helvetica',20,'bold'))
    else:
        canvas.create_text(565,620,text='WRONG!',fill='RED',font=('Helvetica',70,'bold'))
def makeAllPossibleSimpleChangesToMatrix(matrix):
    changes=True
    while changes==True:
        changes=False
        for r in range(MAX):
            for c in range(MAX):
                if Cell.matrix[r][c].TryToReduceCandidateValuesInCell()==True:
                     changes=True
    return matrix
def restoreValues(matrix,oldMatrix):
    for r in range(MAX):
        for c in range(MAX):
            matrix[r][c].value=deepcopy(oldMatrix[r][c].value)
    return matrix

def solveTheSodoku(matrix):
    maxtrix=makeAllPossibleSimpleChangesToMatrix(matrix)
    if solutionIsCorrect(matrix):
            return matrix
    oldCopy=deepcopy(matrix)
    for r in range(MAX):
        for c in range(MAX):
            a,b=coordinatesofCellWithSmallestValuesSet(matrix)
            if (a==-1) or(b==-1):
                return matrix
            candidates=list(Cell.matrix[a][b].value)
            for number in candidates:
                matrix[a][b].value={number}
                matrix=solveTheSodoku(matrix)
                if solutionIsCorrect(matrix):
                    return matrix
                matrix=restoreValues(matrix,oldCopy)
    return matrix
def coordinatesofCellWithSmallestValuesSet(matrix):
    big=10
    sml=2
    bestRow=-1
    bestCol=-1
    for r in range(MAX):
        for c in range(MAX):
            length=len(matrix[r][c].value)
            if sml<=length<big:
                big=length
                bestRow=r
                bestCol=c
    return(bestRow,bestCol)


    #first try and reduce row
    #then by column
    #if any changes at all were made,
#go back to the begining
#check to see if it is correct
    #WRITE THIS

from tkinter import Tk,Canvas,YES,BOTH
from time import clock,sleep
from copy import deepcopy
root=Tk()
canvas=setUpCanvas(root)
MAX=9

def main():
    matrix=createTheSudokuBoard()
    matrix=solveTheSodoku(matrix)
    displayTheSudokuBoard(matrix)
    printVerification(matrix)
#    printElapsedTime()
    root.mainloop()


if __name__ == '__main__':
    main()
