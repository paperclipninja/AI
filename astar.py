#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     27/10/2013
# Copyright:   (c) Arianna 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
graph={     'A':[366,3,('Z',75), ('T', 118),('S',140)],
            'Z':[374,2,('A',75),('O', 71)],
            'T':[329,2,('A',118),('L',111)],
            'L':[244,2,('T',111),('M',70)],
            'M':[241,2,('L',70),('D',75)],
            'D':[242,2,('M',75),('C',120)],
            'C':[160,3,('D',120),('R',146),('P',138)],
            'R':[193,3,('C',146),('P',97),('S',80)],
            'S':[253,4,('R',80),('F',99),('O',151),('A',140)],
            'O':[380,3,('S',151),('Z',71)],
            'P':[100,3,('C',138),('R',97),('B',101)],
            'F':[176,2,('S',99),('B',211)],
            'B':[0,4,('P',101),('F',211),('G',90),('U',85)],
            'G':[77,1,('B',90)],
            'U':[80,3,('B',85),('H',98),('V',142)],
            'H':[151,2,('U',98),('E',86)],
            'E':[161,1,('H',86)],
            'V':[199,2,('U',142),('E',92)],
            'I':[226,2,('V',92),('N',87)],
            'N':[234,1,('I',87)],

    }

def aStar(goal,root):
    Q=[(0+366,root,[root],0)]
    CLOSED={}
    while Q!=[]:
        (fValue, node, path, gValue)=Q.pop(0)
        if node==goal:
            print(path)
            break
        CLOSED[node]=gValue
        for(child,localDist) in graph[node][2:]:
            #(f(node),nodeName,path-from-root-to-node,g(node))=graph[child]
            if child in CLOSED:
                if gValue+localDist>CLOSED[child]:
                    del CLOSED[child]
                    newChild=(graph[child][0]+gValue, child,path+[child],gValue+localDist)
                    Q.append(newChild)
            for tup in Q:
                if tup[1]==child:
                    if gValue+localDist<tup[3]:
                        Q.remove(tup)
                        Q.append((graph[child][0]+gValue, child,path+[child],gValue+localDist))
                    Q.sort()
                    break
            else:
                Q.append((graph[child][0]+gValue, child,path+[child],gValue+localDist))
                Q.sort()

def main():
    print(aStar('B','A'))

if __name__ == '__main__':
    main()
