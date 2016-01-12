#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     20/03/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    from math import tan, atan, atan2, sin, cos, pi, sqrt

    IMAGEHEIGHT=512
    IMAGEWIDTH=512
    m=3
    b=300
    x=30
    y=m*x+b
    assert y ==m*x+b,['Error in initial data: y!=mx+b']
    print('Initial values:m=',m,',b=',b,',x=',x,', and y=',m*x+b,'.', sep=' ')
    phi=atan(m)
    theta=phi-pi/2
    r=x*sin(phi)-y*cos(phi)

    imageDiagonal=sqrt(IMAGEHEIGHT**2+IMAGEWIDTH**2)
    HOUGHHEIGHT=int(imageDiagonal+IMAGEHEIGHT)+1
    HOUGHWIDTH=int((pi/2+pi/2)*100)
    houghLst=[0]*(HOUGHHEIGHT*HOUGHWIDTH)
    print('length of HoughLst is', len(houghLst))

    theatIndex=int((theta+(pi/2))*100)
    rIndex=int(r+IMAGEHEIGHT)
    houghLst[rIndex*HOUGHWIDTH+theatIndex]+=1
    print('\nDEHOUGH! DEHOUGH! DEHOUGH! DEHOUGH! DEHOUGH! DEHOUGH!\n')
    maxIndex=houghLst.index(max(houghLst))
    rIndex=maxIndex//HOUGHWIDTH
    theatIndex=maxIndex%HOUGHWIDTH

    r=rIndex-IMAGEHEIGHT
    theta=theatIndex/100-pi/2
    m=-1/tan(theta)
    b=r/sin(theta)

    print('Recovere values: m=',round(m,2),'b=',round(b,2))
    newY=m*x+b
    percentOfError=((y-newY)/y)*100
    print('x=',x,'andy=',round(newY,2),'. y-error=',round(percentOfError,2),'%',sep=' ')


if __name__ == '__main__':
    from time import clock; START_TIME=clock(); main();
    print('-->Run time=', round(clock()-START_TIME,2),'seconds <--');

