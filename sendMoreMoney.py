#-------------------------------------------------------------------------------
# Name:        send more money
# Purpose:
#
# Author:      Arianna
#
# Created:     17/02/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import itertools


#so... what we want to do...
#is to solve for send+more=money
#so all of the letters can be an integer from 0-9. xcept for s and m, which can't really be zero
#interate through all of the different letter possibilities
# if one works, return the answer
#also going to want to check to make sure that it workes

def sendMoreMoney():
    for s in range(1, 10):
        for e in range(0, 10):
            for n in range(0, 10):
                for d in range(0, 10):
                    for m in range(1, 10):
                        for o in range(0, 10):
                            for r in range(0, 10):
                                for y in range(0, 10):
                                    if isDistinct(s, e, n, d, m, o, r, y):
                                        send = 1000 * s + 100 * e + 10 * n + d
                                        #putting digits into addable format
                                        more = 1000 * m + 100 * o + 10 * r + e
                                        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
                                        if send + more == money:
                                            return send, more, money
def dogCatFight():
    for d in range(1, 10):
        for o in range(0, 10):
            for g in range(0, 10):
                for c in range(1, 10):
                    for a in range(0, 10):
                        for t in range(0, 10):
                            for f in range(1, 10):
                                for i in range(0, 10):
                                    for h in range(0,10):

                                         if isDistinct(c,a,t,d,o,g,f,i,h):
                                            cat = 100 * c + 10 * a +  t
                                        #putting digits into addable format
                                            dog = 100 * d + 10 * o + 1 * g
                                            fight = 10000 * f + 1000 * i + 100 * g + 10 * h + t
                                            if dog*cat == fight:
                                                return dog,cat, fight


def isDistinct(*args):
    return len(set(args)) == len(args)



def main():
    print('dog*cat=fight')
    print(dogCatFight())
    print("Time elapsed= 1 minutes(s), and 50 second(s)")
    #print('send+more=money')
    #print(sendMoreMoney())

if __name__ == '__main__':
    main()
