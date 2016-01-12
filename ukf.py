#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     04/02/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def permutate1(stng):
    if len(stng)==1:
        return stng
    if len(stng)==2:
        return [stng[0]+stng[1],stng[1]+stng[0]]
    substring=permutate1(stng[1:])
    permList=[]
    for q in substring:
        for i in range(len(stng)):
            word=(q[:i]+stng[0]+q[i:])
            if word not in permList:
                permList.append(word)
    return permList

def permutate2(stng):
    if len(stng)==1:
        return stng
    ch=stng[0]
    return[s[:n]+ch+s[n:] for s in permutate2(stng[1:]) for n in range(len(stng))]
def main():
    print(permutate1('AABB'))
    pass

if __name__ == '__main__':
    main()
