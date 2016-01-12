#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     19/12/2013
# Copyright:   (c) Arianna 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# print by number, print by unicode, print by letter in alphabetical order

def setUpcanvas(root):
    root.title("A Tk/Python Graphics Program")
    canvas=Canvas(root, width=1270, height=780, bg='DARK BLUE')
    canvas.pack(expand=YES, fill=BOTH)
    return canvas
def printUnicode(startNumber=0):
    row=22
    col=10
    size=15
    canvas.create_text(125,20,text="UTF-8 (starting at"+str(startNumber)+")",fill='WHITE', font=('Helvetica', 12, 'bold'))
    for r in range(row):
        for c in range(col):
            num=c+r*col+startNumber
            tab=' '*(col-len(str(num))+5)
            canvas.create_text(c*120+48, r*25+45, text=tab+str(num)+"="+ chr(num), fill='GOLD', font=('Helvetica',size,'bold'))
from tkinter import*
root=Tk()
canvas=setUpcanvas(root)

def main():
    print(unicode('a'))
    printUnicode(9728)
    root.mainloop()

if __name__ == '__main__':
    main()
