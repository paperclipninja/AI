#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     29/11/2013
# Copyright:   (c) Arianna 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
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
    def getChildren(self):
        return self.children
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
         while (stng[0] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
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
         while (stng[0] not in 'abcdefghijklmnopqrstuvwxyz'):
                stng=stng[1:]
        if stng=='' and ('$' in self.children):
            return True
        elif stng=='':
            return False
        elif stng[0] in self.children:
            return self.children[stng[0]].search(stng[1:])
        elif '$' not in self.children:
            return False



def printGhostDirections ():
    print('+-------------------------------+')
    print('| Welcome to the game of GHOST. |')
    print('| The human goes first. Enter   |')
    print('| your letters in the pop-up    |')
    print('| dialog boxes. Good Luck.      |')
    print('+-------------------------------+')

def requestandCheckHumanMove(root, stng):
    stng+=input('HUMAN, endter your character.').lower()[0]
    print(' ',stng)
    if root.search(stng)==True:
        print('-------------------------------------')
        print('HUMAN LOSES because"',stng,'"is a word.', sep='')
        print('-------------<GAME OVER >------------')
        exit()
    if fragmentInDictionary(root, stng) ==False:
        print('-------------------------------------')
        print('HUMAN LOSES because"',stng,'"does not begin any word.', sep='')
        print("[The computer's word was",'"', spellWordFromString(root, stng[0:-1]),'".]',sep='')
        print('-------------<GAME OVER >------------')
        exit()
    return (stng)
from copy import deepcopy
def spellWordFromString(self, stng):
    strin=deepcopy(stng)
    node=self
    while stng!='':
        node=node.children[stng[0]]
        stng=stng[1:]
    n=randomChild(node)
    while n!='$':
        strin+=n
        node=node.children[n]
        n=randomChild(node)

    return strin
 #   disposable=deepcopy(stng)
  #  if disposable!='':
   #     searchForNextLetter(self.children[disposable[0]],disposable[1:])
    #a=randomChild(self)
#    node=self
 #   while a.value!=('$'):
  #      stng+=a
   #     b=randomChild(node.children[a])
    #    node=node.children[b]
     #   stng+= b
      #  a=deepcopy(b)

def createTrieFromDictionaryFile():
    root=Node('*')
    file1=open('dictionary.txt')
    for word in file1:
        root.insert(word.lower().strip())
    file1.close
    return root
from random import choice
def randomChild(self):
    a= choice(list(self.children.keys()))
    return a
    #used by computer to choose a random letter from children of th current node. us the !choice() function from the random library
def searchForNextLetter(self,stng):
    node=self
    while stng!='':
        node=node.children[stng[0]]
        stng=stng[1:]
    return randomChild(node)
    #recursive
    #runs through the tree to final character in stng, then calls random child to choose one of the letters. STNG is passed through funtion, not just leter
def fragmentInDictionary(self,stng):
    if stng!='':
         while (stng[0] not in 'abcdefghijklmnopqrstuvwxyz'):
                stng=stng[1:]
    if stng=='' and ('$' in self.children):
            return True
    elif stng=='':
            return True
    elif stng[0] in self.children:
            return fragmentInDictionary(self.children[stng[0]],stng[1:])
    elif '$' not in self.children:
            return False

    #recursive
    #checks that stng is in the trie as a fragment that would ultimatley spell a word.
    #otherwise computer loses. Can't happen to computer because always makes legit strings or spells a word and fails


def requestandCheckComputerMove(root,stng):

    stng+=searchForNextLetter(root,stng)
    print(' ',stng)
    if root.search(stng)==True:
        print('-------------------------------------')
        print('COMPUTER LOSES because"',stng,'"is a word.', sep='')
        print('-------------<GAME OVER >------------')
        exit()
    return (stng)

def main():
    root= createTrieFromDictionaryFile()
    printGhostDirections()
    stng=''
    while True:
        stng=requestandCheckHumanMove(root,stng)
        stng=requestandCheckComputerMove(root,stng)

if __name__ == '__main__':
    main()
