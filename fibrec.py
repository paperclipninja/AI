#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     06/09/2013
# Copyright:   (c) Arianna 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
''''
def fibRec( n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibRec(n-1)+fibRec(n-2)
'''
def main():
#    print(fibRec(12))

   # num= int(input('Number?'))
   # print(num+1)
    list=[1,2,3,4]
    ls=[4,3,2,1]
    print(list)
    print(ls)

if __name__ == '__main__':
    main()