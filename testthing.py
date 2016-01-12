#-------------------------------------------------------------------------------
# Author:      Arianna Sze
#
# Created:     11/12/2013
#-------------------------------------------------------------------------------

def main():
    a=1
    str=''
    for a in range(1,101):
        str=a
        if a%3==0:
            str="Fizz "
        if (a%3==0) and (a%5==0):
            str+="and Buzz"
        elif a%5==0:
            str='Buzz'
        if a==0:
            str=''
        print(str)
#IT WORKS!
#THey might not higher the highest scorer because:
#1. Not as much to learn
#2 Already talented
#3. could be let go because learned all they could from intern program
if __name__ == '__main__':
    main()
