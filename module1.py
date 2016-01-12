#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     06/03/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import*
from time import clock
from sys import setrecursionlimit
setrecursionlimit(7000)
root=  Tk()
START=clock()
WIDTH=512
HEIGHT=512
COLORFLAG=False
LOW=10
NUMBER_OF_TIMES_TO_SMOOTH_IMAGE=6

class ImageFrame:
    def __init__(self,image):
        self.img=PhotoImage(width=WIDTH,height=HEIGHT)
        for row in range(HEIGHT):
            for col in range(WIDTH):
                num=image[row*WIDTH+col]
                if COLORFLAG==True:
                    kolor='#%02x%02x%02x'% (num[0],num[1],num[2])
                else:
                   kolor='#%02x%02x%02x'% (num,num,num)
                self.img.put(kolor, (col,row))
        c=Canvas(root, width=WIDTH,height=HEIGHT); c.pack()
        c.create_image(0,0, image=self.img, anchor=NW)
        printElapsedTime('displayed image')

def printElapsedTime(msg='time'):
    length=30
    msg=msg[:length]
    tab='.'*(length-len(msg))
    print('--'+msg.upper()+tab+' ',end='')
    time=round(clock()-START,1)
    print('%2d'%int(time/60),' min :','%4.1f'%round(time%60,1),' sec', sep='')

def displayImageInWindow(image):
    global x
    x=ImageFrame(image)

def main():
    imageFileName=print()

if __name__ == '__main__':
    main()
