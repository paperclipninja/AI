#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     14/12/2013
# Copyright:   (c) Arianna 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import*

def setUpCanvas(root):
    root.title("Wolfram's cellular automata: A Tk/Python Graphics Program")
    canvas=Canvas(root, width=1270, height = 780, bg='black')
    canvas.pack(expand=YES, fill=BOTH)
    return canvas
def convertToBinary(L):
    a=[]
    p=0
    for n in range(len(L)-2):
       if L[n]==1:
            p+=4
       if L[n+1]==1:
        p+=2
       if L[n+2]==1:
        p+=1
        a.add(p)
        p=0

def printList(rule):
#1. print title
    canvas.create_text(170,20,text='Rule'+str(rule), fill='gold',font=('Helvetica',20,'bold'))
    #2 set up list(L) and print the top row.
    L=[1,]
    canvas.create_text(650,10,text=chr(9607), fill='RED', font=('Helvetica',FSIZE,'bold'))
    #3. WRITE THE REST
    L=[0,0]+L+[0,0]
    for row in range(100):
        for n in range(len(L)):
            if L[n]==0:
                kolor=('BLACK')
            if L[n]==1:
                kolor=('RED')
            canvas.create_text(650-row*FSIZE+FSIZE*n,row*FSIZE+10, text=chr(9607),fill=kolor,font=('Helvetica',FSIZE,'bold'))
        #printing things
        #print(L)
        a=[]
        newL=[]
        for p in range(len(L)-2):
            stng=str(L[p])+str(L[p+1])+str(L[p+2])
           # print(p,end=' ')
            #print(stng,end=' ')
           # print(int(stng,2))
            newL+=[rule[len(rule)-1-int(stng,2)]]
        L=[0,0]+newL+[0,0]
    #look at 3 at a time, binary numbers
    #then take htose numbers, and look in 'rule' for the corresponding numbers. if it's 1, Red 0,black
    #then print everything

    #chr(9670), fill=red==block
    #print small solid red rectangle chr(9670) for each 1
    # for each 0, print solid black rectangle

root=Tk()
canvas=setUpCanvas(root)
FSIZE=8
def main():
    rule=[0,1,1,0,1,1,1,0,]
    printList(rule)
    root.mainloop()


if __name__ == '__main__':
    main()
