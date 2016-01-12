#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     31/10/2013
# Copyright:   (c) Arianna 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def repeatingDecimalToFraction(number,repLength):
    if isinstance(number,(str )):
        return("ERROR"),(" in repeating decimal")
    stng=str(number)
    index=stng.find('.')
    decLeng=len(stng)-index-1
    length=decLeng-repLength
    if decLeng < repLength:
        return("ERROR"),(" in repeating decimal")
    if isinstance(repLength,(float,str)):
        return("ERROR"),(" in repeating decimal")
    if repLength==0:
        #print(int(number*(10**decLeng)))
        #print(num*(10**len(stng))-int(num*(10**len(stng))))
        return int(number*(10**decLeng)), 10**(decLeng)
    else:
        print(int(number*(10**length)))
        print(int((10**repLength)*(number*(10**length)-int(number*(10**length)))))
        n,d= fraction(int(number*(10**length)), int((10**repLength)*(number*(10**length)-int(number*(10**length)))))
        return n, d*(10**length)
    #number*(10**(decLeng-repLength)), 10**(decLeng-repLength)


def fraction(intPart, decPart):
    #the integer part=something
    #Denominator is:
    #repeating decimal is decPart
    if intPart!=0:
        fct=10**len(str(intPart))
    else:
        fct=10**len(str(decPart))
    decPart=decPart/(10**len(str(decPart)))
    d=decPart
    for a in range(10):
        d=decPart+d/fct
    d+=intPart
    numerator=fct*d-d
    denom=fct-1
    print(denom)
    return int(numerator+.5), denom

def main():

    num,den =  repeatingDecimalToFraction(2.1,1)
    #print(intpart, decpart)
    #num,den = fraction(intpart,decpart)
    print ('answer=',str(num)+'/'+str(den))

if __name__ == '__main__':
    main()
