#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     03/04/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import*
from time import clock
#--<GLOBALS>-----
root=Tk()
START=clock()
from math import *
WIDTH=512
HEIGHT=512
imageDiagonal=sqrt(HEIGHT**2+WIDTH**2)
HOUGHWIDTH=int((pi/2+pi/2)*100)
HOUGHHEIGHT=int(imageDiagonal+HEIGHT)+1
from math import pi, sqrt
angleRange=int(2*pi/0.01)
radiusRange=int(sqrt(2)*512)
class ImageFrame:
    def __init__(self, image):
        self.img=PhotoImage(width=WIDTH,height=HEIGHT)
        for row in range(HEIGHT):
            for col in range(WIDTH):
                num=image[row*WIDTH+col]
                if num==255 or num<252:
                    kolor='#%02x%02x%02x'%(num,num,num)
                if num==254:
                    kolor='#%02x%02x%02x'%(num,0,0)
                if num==253:
                    kolor='#%02x%02x%02x'%(0,num,0)
                if num==252:
                    kolor='#%02x%02x%02x'%(0,0,num)
                if not(0<=num<256):
                    exit('ERROR: num='+num)
                self.img.put(kolor, (col,row))
        c=Canvas(root,width=WIDTH,height=HEIGHT);c.pack()
        c.create_image(0,0, image=self.img,anchor=NW)
        printElapsedTime('Displayed Image')
def frange(start, stop, step):
    i=start
    terminate=stop-(step/10)
    while i<terminate:
        yield i
        i+=step
def drawLine(m,b,image,start=0,stop=512,color=255):
    from math import sin
    for x in range(start, stop):
        row=int(m*x+b)
        try:
            image[row*WIDTH+x]=255
        except:
            pass

def main():
     image=[0 for elt in range(HEIGHT*WIDTH)]

if __name__ == '__main__':
    main()
