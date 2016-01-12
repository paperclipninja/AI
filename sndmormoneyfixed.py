#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Arianna
#
# Created:     18/02/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from itertools import*
from time import*
from re import*
from math import*
def solve (puzzle):
    count=1
    puzzle=puzzle.upper()
    words=findall('[a-z]+',puzzle)
    start=clock()
    unique_characters=set(''.join(words))
    #get unique characters
    first_letters={word[0] for word in words}
    n=len(first_letters)
    sorted_characters=''.join(first_letters)+''.join(unique_characters-first_letters)
    characters=tuple(ord(c) for c in sorted_characters)
    print(characters)
    digits=tuple(ord(c) for c in '0123456789')
    zero=digits[0]
    Lst=permutations(digits,len(characters))
    for guess in Lst:
        equation=puzzle.translate(dict(zip(characters,guess)))
        if eval(equation):
            return equation



def main():
    start=clock()
    puzzle="DOG*CAt==FIGHT"
    print("Puzzle:",puzzle)
    print("The solution (if any) follow:")
    solve(puzzle)
    print("---------------------------------")
    stop=clock()
    seconds=stop-start
    print("Time elapsed=", floor(seconds/60), "minutes(s), and", round(seconds%60,1),"second(s)")

if __name__ == '__main__':
    main()
