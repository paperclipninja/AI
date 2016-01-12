#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     11/03/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
ROW=8
COL=8
def createList():
    image=[0]*ROW*COL
    for r in range(ROW*COL):
        image[r]=int(r)
    return image
def printList(image):
    for c in range(ROW):
        for r in range(COL):
            #print('number',(r+c*COL))
            print('%3d'%image[r+c*COL],end='')
        print('')
def createNewImage():
    image=[]
    for i in range(ROW*COL):
        image.append(0)
    return image
def runMask(image,newImage):
    for r in range(1,COL-1):
        for c in range(1,ROW-1):
            print('r',r,'c',c)
            print(r+c*COL)
            print((r+(c-1)*COL)+(r+1+(c)*COL))
            newImage[r+c*COL]=(r+(c-1)*COL)+(r+1+(c)*COL)
    return newImage
def main():
    image=createList()
    print(image)
    printList(image)
    newImage=createNewImage()
    printList(newImage)
    print()
    newImage=runMask(image,newImage)
    printList(newImage)

if __name__ == '__main__':
    main()
