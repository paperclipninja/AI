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

  #  print('NOT WORKING')

#def imageNoise(points, image):
 #   for n in range(points):
  #      x=randint(0,WIDTH)
   #     y=randint(0,HEIGHT)
    #    image[x*WIDTH+y]=255
def phiF():
    from math import pi,atan
    phi=[]
    for p in frange(0,2*pi,.1):
        phi[p*10]=(atan(p))
    yield phi

def houghTransform(image, accumulator):
    from math import pi, sin, cos
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if image[x*WIDTH+y]==255:
                for phi in frange(0,2*pi,.1):
                    theta=phi-pi/2
                    r=(x*sin(phi)-y*cos(phi))
                    thetaIndex=int((theta+pi/2)*100)
                    rIndex=int(r+HEIGHT)
                    accumulator[int(r*HOUGHWIDTH+thetaIndex)]+=1

def deHoughIndex(index):
    from math import sin, cos
    rIndex=index//HOUGHWIDTH
    thetaIndex=index%HOUGHWIDTH

    r=rIndex-HEIGHT
    theta=thetaIndex/100-pi/2

    m=-1*tan(theta)
    b=r/sin(theta)+10
    return m,b
def indexOfLocalMaximums(accumulator):
    big=max(accumulator)
    indices=[]
    for x in range(len(accumulator)):
        if accumulator[x]==big:
            indices.append(x)
    return indices

def main():
    image=[0 for elt in range(HEIGHT*WIDTH)]

   # imageNoise(500, image)

    #drawLine(0, 256, image)
    drawLine(0.57, 66.7, image)
    #drawLine(-1,500,image,100,200)

    accumulator=[0 for elt in range(angleRange*radiusRange)]
   # print(accumulator)
    houghTransform(image,accumulator)
    print(houghTransform)
    indices=indexOfLocalMaximums(accumulator)

    print('Number of indices=',len(indices))
    for i in indices:
        m,b= deHoughIndex(i)
        print(-m,' m ',b/25,' b')
        drawLine(-m,b/25, image)
    #dehough stuff here
#dehough returns m, b

#finish stuff

    x=ImageFrame(image)
    root.mainloop()


if __name__ == '__main__':
    main()
