#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     10/12/2013
# Copyright:   (c) Arianna 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
root=Tk()
canvas=setUpCanvas(root)
FSIZE=8
def setUpCanvas(root):
    root.title("Wolfram's cellular automata: A Tk/Python Graphics Program")
    canvas=Canvas(root,width=1270,height=780, bg='black')
    canvas.pack(expand=YES,fill=BOTH)
    return canvas
def printList(rule):
#1 print the title
    canvas.create_text(170,20,text="Rule"+str(rule), fill='gold',font=('Helvetica',20,bold))
    L=[1,]
    canvas.create_text(650,10,text=chr(9670),fill='RED',font=('Helvetica',FSIZE,'bold'))
    #WRITE THE REST

def main():
    ##rule=[0,0,0,1,1,1,1,0,] #rule 30=strange
    ##rule=[0,1,0,1,1,0,1,0,] #rule 90=pretty picture
    ##rule=[0,1,1,0,1,1,1,0,] #rule 90=pretty picture
    ##rule=[0,1,1,0,1,1,1,0,] #rule 90=pretty picture
      rule=[1,1,1,1,1,1,1,1,] #rule 90=pretty picture
      printList(rule)
      root.mainloop()

if __name__ == '__main__':
    main()
