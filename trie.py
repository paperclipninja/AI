#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     18/11/2013
# Copyright:   (c) Arianna 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from time import clock
class Node(object):
    def __init__(self, value):
        self.value=value
        self.children={}
    def __repr__(self):
        self.print()
        return''
    def print(self, stng):
        for keys in self.children:
            if self.children[keys].value != '$':
                self.children[keys].print(stng+self.children[keys].value)
            elif self.children[keys].value =='$':
                print( stng)

        #recursively print all words in the Trie
    def display(self):
        if self.value=='$':
            return

        print('==========NODE==========')
        print('-->self.value   =',self.value)
        print('-->self.children:[',end='')
        for keys in self.children:
            if keys !='$':
                print(keys,sep='',end=',')
        print(']')
        print('------------------------')
        for char in self.children:
            (self.children[char]).display()
    def insert(self, stng):
        if stng!='':
         while (stng[0] not in 'abcdefghijklmnopqrstuvwxys'):
                stng=stng[1:]
        if stng=='':
            a=Node('$')
            self.children[a.value]=a


        elif stng[0] not in self.children:
            p=Node(stng[0])

            self.children[stng[0]]=p
            p.insert(stng[1:])
        else:
            self.children[stng[0]].insert(stng[1:])


    def search(self,stng):
        if stng!='':
         while (stng[0] not in 'abcdefghijklmnopqrstuvwxys'):
                stng=stng[1:]
        if stng=='' and ('$' in self.children):
            return True
        elif stng=='':
            return False
        elif stng[0] in self.children:
            return self.children[stng[0]].search(stng[1:])
        elif '$' not in self.children:
            return False

def main():
    root=Node('*')
    root.insert('cat')
    root.insert('catnip')
    root.insert('catnap')
    root.insert("can't")
    root.insert('cat-x')
    root.insert('dog')
    root.insert('dogs')
    root.insert('dognip')
    root.print('')
    #root.display()
    print('SEARCH:',root.search('cat'))
    printElapsedTime()
def printElapsedTime():
    print('\n ---Total run time=',round(clock()-startTime,2),'seconds.')

    pass

if __name__ == '__main__': startTime=clock(); main()
