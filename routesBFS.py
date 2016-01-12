#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     15/10/2013
# Copyright:   (c) Arianna 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from time import clock
graph={'A':[('Z',75), ('T', 118),('S',140)],
            'Z':[('A',75),('O', 71)],
            'T':[('A',118),('L',111)],
            'L':[('T',111),('M',70)],
            'M':[('L',70),('D',75)],
            'D':[('M',75),('C',120)],
            'C':[('D',120),('R',146),('P',138)],
            'R':[('C',146),('P',97),('S',80)],
            'S':[('R',80),('F',99),('O',151),('A',140)],
            'O':[('S',151),('Z',71)],
            'P':[('C',138),('R',97),('B',101)],
            'F':[('S',99),('B',211)],
            'B':[('P',101),('F',211),('G',90),('U',85)],
            'G':[('B',90)],
            'U':[('B',85),('H',98),('V',142)],
            'H':[('U',98),('E',86)],
            'E':[('H',86)],
            'V':[('U',142),('E',92)],
            'I':[('V',92),('N',87)],
            'N':[('I',87)],

    }

def BFS_AnyPath(Q, closedSet=[]):
#Q=[('A','B',['A'],0)]
    node,goal,path,d=Q.pop(0)
    closedSet.append(node)
#return stuff in the form child+path....
    for(child, dist) in graph[node]:
       if child not in closedSet:
          p2=path+[child]; di=dist+d;
          if child==goal:
            return [child, goal, p2, di],closedSet
          Q.append([child, goal, p2, di])

    return BFS_AnyPath(Q,closedSet)


def BFS_LeastCostPath(start,goal):
    curent, path, cost=start,[start],0
    Q=[(start,[start],cost)]
    bestleastCost=(start, 10000000)
    while not Q==[]:
        curent, path, cost=Q.pop(0)
        for(child, dist) in graph[curent]:
            if child==goal and cost+dist<=bestleastCost[1]:
                    bestleastCost=[path+[child], cost+dist]
            if child not in path:
                if cost+dist<=bestleastCost[1]:
                    Q.append([child,path+[child],cost+dist])

    return bestleastCost




def main():
    print('  == BFS SEARCHING == ')
    Q=[('A','B',['A'],0)] #first two=start+goal. 2nd=path. 0=distance
    print("The FEWEST-NODE path from 'A' to 'B' is",BFS_AnyPath(Q)[0][2])
    print("\nThe SHORTEST  path from'A' to 'B' is",BFS_LeastCostPath('A','B'))
    print('\n---TOTAL search time=',round(clock()-startTime,2),'seconds.')


if __name__ == '__main__':startTime=clock(); main()
