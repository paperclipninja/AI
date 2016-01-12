
#
# Author:      Arianna
#
# Created:     12/12/2013

#-------------------------------------------------------------------------------

def bogusFunction(stng):
    diCt={}
    for n in range(len(stng)):
        s=stng[n:n+1]
        #get the individual character
        if s not in diCt.keys():
            diCt[s]=1
            # insert character into dictionary if not already in
        else:
            diCt[s]+=1
            #add to the number of times s appears in stng
    return len(diCt.keys()), diCt
def main():
    num,di=bogusFunction('SUPERCALIFRAGILISTICEXPIALIDOCIOUS')
    print('Number of Characters:',num)
    print('')
    print('----------Characters and Count----------')
    for letter in di.keys():
        print('|    Letter',letter,' Appears ', di[letter],'Time(s)       |')
    print('----------------------------------------')


Number of Characters: 15
----------Characters and Count-----------
|   letter C  appears  3 time(s)        |
|   letter A  appears  3 time(s)        |
|   letter G  appears  1 time(s)        |
|   letter F  appears  1 time(s)        |
|   letter E  appears  2 time(s)        |
|   letter D  appears  1 time(s)        |
|   letter I  appears  7 time(s)        |
|   letter O  appears  2 time(s)        |
|   letter L  appears  3 time(s)        |
|   letter S  appears  3 time(s)        |
|   letter R  appears  2 time(s)        |
|   letter P  appears  2 time(s)        |
|   letter U  appears  2 time(s)        |
|   letter T  appears  1 time(s)        |
|   letter X  appears  1 time(s)        |
-----------------------------------------

if __name__ == '__main__':
    main()
