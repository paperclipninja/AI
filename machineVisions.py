#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     20/02/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import*
from time import clock
from math import *
from copy import deepcopy
from sys import setrecursionlimit
setrecursionlimit(7000)
root=  Tk()
START=clock()
WIDTH=512
HEIGHT=512
COLORFLAG=False
HIGH=35
LOW=25
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
def normalize(image,intensity=255):
    m=max(image)
    printElapsedTime('normalizing')
    return[int(x*intensity/m) for x in image]
def sobelMask(image):
    image2=[[0,0,0,0,0]for elt in range(HEIGHT*WIDTH)]
    print('attempting sobelmask...')
    for row in range(1,HEIGHT-1):
        for col in range(1, WIDTH-1):
            #print('trying sobel mask in for loop')
            Gy=image[(row+1)*WIDTH+col]*-2+image[(row-1)*WIDTH+col]*2+image[(row+1)*WIDTH+col+1]*-1+image[(row-1)*WIDTH+col+1]+image[(row+1)*WIDTH+col-1]*-1+image[(row-1)*WIDTH+col-1]
           # print('GY',Gy)
            Gx=image[row*WIDTH+col-1]*-2+image[row*WIDTH+col+1]*2+image[(row+1)*WIDTH+col+1]+image[(row-1)*WIDTH+col+1]+image[(row+1)*WIDTH+col-1]*-1+image[(row-1)*WIDTH+col-1]*-1
            #Gx=image[row*WIDTH+col-1]*-2+image[row*WIDTH+col+1]*2+image[(row+1)*WIDTH+col+1]+image[(row-1)*WIDTH+col+1]+image[(row+1)*WIDTH+col-1]*-1+image[(row-1)*WIDTH+col-1]*-1
            #print('GX',Gx)
            m = int(round(sqrt(Gx*Gx+Gy*Gy)))
            d =theta(Gx,Gy)
            image2[row*WIDTH+col] = [m, d, 0,0,0]

    #displayImageInWindow(mags)
    #mags=normalize([x for x in image])
    #x=ImageFrame(mags)
    return image2
def theta(x,y):
    angle=atan2(y,x)
    if angle>pi or angle<0:
        angle=angle+pi
    if angle<abs((pi/4)-angle) or (abs(pi-angle)<abs(3*pi/4-angle)):
        return 0
    if abs((pi/4)-angle)<abs(pi/2-angle):
        return 1
    elif abs(pi/2-angle)< abs(3*pi/4-angle):
        return 2
    else:
        return 3
def processAngles(image):

    for row in range(1, HEIGHT-1):
        for col in range(1, WIDTH-1):
            ang=image[row*WIDTH+col][1]
            if ang==1:
                if image[row*WIDTH+col][0]> image[(row+1)*WIDTH+col+1][0] and (image[row*WIDTH+col][0]> image[(row-1)*WIDTH+col-1][0]):
                    image[row*WIDTH+col][2]=1
                #compare the one rihgt and up
                #compare teh one left and down

            if ang==2:
                if image[row*WIDTH+col][0]> image[(row+1)*WIDTH+col][0] and (image[row*WIDTH+col][0]> image[(row-1)*WIDTH+col][0]):
                    image[row*WIDTH+col][2]=1
                #compare up and down
                #print('FIX ME')
            if ang==3:
                if image[row*WIDTH+col][0]> image[(row-1)*WIDTH+col+1][0] and (image[row*WIDTH+col][0]> image[(row+1)*WIDTH+col-1][0]):
                    image[row*WIDTH+col][2]=1
                #compare right and down
                #compare left and up
                #print('FIX ME')
            if ang==0:
                if image[row*WIDTH+col][0]> image[(row)*WIDTH+col+1][0] and (image[row*WIDTH+col][0]> image[(row)*WIDTH+col-1][0]):
                    image[row*WIDTH+col][2]=1
                #compare l and R
               # print('FIX ME')
    return image
def cannyTransform(image):
    print('trying to canny transform...')
    image=processAngles(image)
    #edit me
    #list in tferms of magnitude, angle appdroximafion (theta 1, 2, 3, or 0), Been here YoN, printedyet YoN
    for row in range(1,HEIGHT-1):
        for col in range(1, WIDTH-1):
            #print("it might be working")
            if image[row*WIDTH+col][2]==1 and image[row*WIDTH+col][0]>HIGH:
               # print("step1")
                image[row*WIDTH+col][4]=1
                fixCellAt(image,row,col)
    newLst=[0]*HEIGHT*WIDTH
    for row in range(1, HEIGHT-1):
        for col in range(1,WIDTH-1):
            if(image[row*WIDTH+col][2]==1 and image[row*WIDTH+col][4]==1):
                #print("it might be working!")
                newLst[row*WIDTH+col]=250
    return newLst
    #print(image2)
   # return image
def fixCellAt(M, row, col):
    if M[(row)*WIDTH+col][3]==1:
        M[(row)*WIDTH+col][3]=1
        return
    if(row>0 and M[(row-1)*WIDTH+col][2]==1 and M[(row-1)*WIDTH+col][0]>LOW):
        M[(row-1)*WIDTH+col][3]=1
        M[(row-1)*WIDTH+col][4]=1
        fixCellAt(M, row-1, col)
    if(row>0 and M[(row)*WIDTH+col-1][2]==1 and M[(row)*WIDTH+col-1][0]>LOW):
        M[(row)*WIDTH+col-1][3]=1
        M[(row)*WIDTH+col-1][4]=1
        fixCellAt(M, row, col-1)
    if(row>0 and M[(row+1)*WIDTH+col][2]==1 and M[(row+1)*WIDTH+col][0]>LOW):
        M[(row+1)*WIDTH+col][3]=1
        M[(row+1)*WIDTH+col][4]=1
        fixCellAt(M, row+1, col)
    if(row>0 and M[(row)*WIDTH+col+1][2]==1 and M[(row)*WIDTH+col+1][0]>LOW):
        M[(row)*WIDTH+col+1][3]=1
        M[(row)*WIDTH+col+1][4]=1
        fixCellAt(M, row, col+1)
   # print("step 2")
#high 10
#low 6
def main():
    file1=open('lena.ppm','r')
    stng=file1.readline().strip()
    print(stng)
    nums=file1.read().split()
    print(nums[:10])
    file1.close()
    #exit()
    image=[]
    for pos in range(0,len(nums),3):
                 RGB=(int(nums[pos+0]), int(nums[pos+1]),int(nums[pos+2]))
                 image.append(int(0.2*RGB[0]+.7*RGB[1]+.1*RGB[2]))
                 #printElapsedTime('grey numbers are now created')
    displayImageInWindow(image)
    file1=open('grayScale.ppm','w')
    for elt in image:
    #    file1.write(str(elt)+' ')
   # printElapsedTime('Grey numbers are now created')
   # file1.close()
   # image3=deepcopy(image)
   # image2=[0]*WIDTH*HEIGHT
   # for n in range(6):
    # for row in range(1,HEIGHT-1):
     #   for col in range(1, WIDTH-1):
      #      image2[row*WIDTH+col]=image3[row*WIDTH+col]*4/16+image3[row*WIDTH+col-1]*1/8+image3[row*WIDTH+col+1]*1/8+image3[(row+1)*WIDTH+col]*1/8+image3[(row-1)*WIDTH+col]*1/8+image3[(row+1)*WIDTH+col+1]*1/16+image3[(row-1)*WIDTH+col+1]*1/16+image3[(row+1)*WIDTH+col-1]*1/16+image3[(row-1)*WIDTH+col-1]*1/16
    # image3=deepcopy(image2)

   # image3=sobelMask(deepcopy(image3))
   # image3=cannyTransform(image3)
   # displayImageInWindow(image3)
    #print(image3)
   # root.mainloop()
#http://imgur.com/gallery/kGy1HwX
#http://imgur.com/gallery/7bz5Lk9
#imgur.com/gallery/7bz5Lk9
#imgur.com/gallery/7bz5Lk9
if __name__ == '__main__':
    main()
