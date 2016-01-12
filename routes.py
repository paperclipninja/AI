from time import clock


import time
def DFS_AnyPath(node, goalNode,path=[],closedSet=[]):
  path=path+[node]
  closedSet.append(node)
  if node==goalNode:
    return path
  else:
    for (child, dist) in graph[node]:
        if child not in closedSet:
            path= DFS_AnyPath(child,goalNode,path,closedSet)
            n=path.pop()
            if n!=None:
                if n==goalNode:
                    return path+[n]
    path.pop()
    return path+[None]
            #NOT QUITE WORKING!!

       #if new[-1].equals(goalNode):
        #    return
       #else:
        #    return path

def DFS_FewestNodesPath(node, goalNode, currentPath=[],bestPath=[]):
   currentPath=currentPath+[node]
   for (child, dist) in graph[node]:
        if child not in currentPath:
            currentPath, bestPath= DFS_FewestNodesPath(child,goalNode,currentPath, bestPath)
            n=currentPath.pop()
            if n==goalNode:
                    if bestPath==[] or len(bestPath)>len(currentPath):
                        bestPath=(currentPath+[n])

   return currentPath,bestPath

def DFS_PathOfLeastCost(node, goalNode, currentPath=[],curCost=0, bestPath=[],lcost=99999999):
  #if type(node)==str:
   # node=(node,0)
  currentPath=currentPath+[node[0]]
  if node[0]==goalNode:
    return currentPath,bestPath,lcost,curCost
  currentPath=currentPath+[node]
  for (child, dist) in graph[node[0]]:
        if child not in currentPath:
            currentPath, bestPath,lcost,curCost= DFS_PathOfLeastCost(child,goalNode,currentPath,curCost+dist, bestPath,lcost)
        if curCost<=lcost:
            bestPath=(currentPath+[child])
            lcost=curCost
  return currentPath,bestPath, lcost,curCost

def DFS_AllPaths(node, goalNode, newPath=[],pathsList=[]):
  newPath=newPath+[node]
  # if node==goalNode:
   # return currentPath
   #else:
  # bestPath=[]
  for (child, dist) in graph[node]:
        if child not in newPath:
            newPath, pathsList= DFS_AllPaths(child,goalNode,newPath, pathsList)
            n=newPath.pop()
            if n==goalNode:
                pathsList.append(newPath+[goalNode])
                        #return currentPath+[n],bestPath

  return newPath,pathsList

  #EXPONENTIAL EXPLOSION

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




def printResults(root,goal,path1,path2,path3,distance,pathsList):
  print('==DFS SEARCHING==')
  print('1. Random 	path from',root,'to',goal,'is', path1)
  print('2. Fewest-nodes path from',root,'to',goal,'is',path2)
  print('3. Shortest-dist path from', root, 'to', goal, 'is',path3,'(',distance,'km.)')
  if pathsList==[]:
    print('4. there are no paths.')
    return
  print('4. all paths from',root,'to',goal,'are listed below.')
  count=0
  pathsList.sort(key=len) #write this one first
  for path in pathsList:
    count+=1
    print('--%2'%count,'. ',path, sep='')
  print('\n---TOTAL search time=',round(clock()-startTime,2),'seconds.')

def main():
  startTime=0;
  root='A';goal='B'
  path1=DFS_AnyPath(root,goal)
  p, path2=DFS_FewestNodesPath(root,goal)
  cp, path3,cost,cd =DFS_PathOfLeastCost(root,goal)
  p, pathList=DFS_AllPaths(root,goal)
  #printResults(root,goal,path1,path2,path3,distance,pathList)
  print('1. Random path from',root,'to',goal,'is',path1)
  print('2. shortest path from',root,'to',goal,'is',path2)
  #print('3. All Paths',,'to',goal,'is',pathList)
  print('4. Shortest distance',root,'to',goal,'is',path3,cost)
if __name__=='__main__':startTime=clock(); main()