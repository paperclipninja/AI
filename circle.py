#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     25/03/2014
# Copyright:   (c) Arianna 2014
#Licence:     <your licence>
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
    def __init__(self, colors, wd=WIDTH, ht=HEIGHT,colorFlag=False):
        self.img=PhotoImage(width=wd,height=ht)
        for row in range(ht):
            for col in range(wd):
                num=colors[row*wd+col]
                if colorFlag==True:
                    kolor='#%02x%02x%02x'%(num[0],num[1],num[2])
                else:
                    kolor='#%02x%02x%02x'%(num,num,num)
                self.img.put(kolor,(col,row))
        c=Canvas(root, width=wd, height=ht);c.pack()
        c.create_image(0,0,image=self.img,anchor=NW)
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

from math import*
def main():
    image=[0 for elt in range(HEIGHT*WIDTH)]
    x= WIDTH
    y=HEIGHT
    radius=150
    for theta in frange(0,2*pi,.1):
        for r in range(radius):
            Gx=x+r*cos(theta)
            Gy=y+r*sin(theta)
            image[int(Gx*WIDTH+Gy)]=255
    #center x=center+rcos(theta)
    #center y= center+sin(theta)r
    #actual
    #position=accumulator.index(max(accumulator))
   # radius=sqrt(())

    x=ImageFrame(image)
    root.mainloop()


if __name__ == '__main__':
    main()
