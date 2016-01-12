class Cost():
  def cost(self):
## return self._data[0]				#special test case for dubugging
## return self._data[0]**2+self._data[1]**2	#special cost function with no domain limits
    from math import sin
    if(0< self._data[0]<10) and (0 < self._data[1]<10):
      return (self._data[0] * sin(4*self._data[0])+1.1*self._data[1]*sin(2*self._data[1]))
    return float('inf')
    
  def sort(A,B,C):
      if B.cost() > C.cost(): B.swap(C)
      if A.cost() < B.cost(): A.swap(B)
      if A.cost() < C.cost(): A.swap(C)
      return [B,C,A]
    
  def sortList(vectorList):
      if type(vectorList)!=list:
        exit('ERROR: The Cost.sort function is limited to a list of elements.')
      vectorList.sort(key=Vector.cost)
      return vectorList
  #returns the smaller of two vectors notation: Vector.minVec(A,B) and A.minVec(B)
  
  def minVec(self, V):
    if self.cost() < V.cost(): return self
    return V
  ########END OF COST CLASS
  
  
  ########START OF VECTOR CLASS
  
  #Notation: X= Vector (1,2), and Y= Vector(X), where X is a list of scalars type both work.
  #The key parameter in a vector is _data, which is a list of the vectors scalar'ss. Do NOT write code
  
class Vector(Cost):
  def __init__(self, *_data):
     if type(_data[0])==Vector:
        self._data=list(_data[0])
        return
     if type(_data[0])==list:
        self._data=_data[0]
        return
     if type(_data[0])==tuple:
        self._data=list(_data[0])
        return
     self._data=list(_data)
      
      
 #print(V) prints a vector's scalars as a list: [1,2,3]
  def __repr__(self):
     return repr(self._data)
 #V.print() prints a Vector with its type name and each scalar rounded to n decimal digits
  def print(self, n=2):
     print("Vector<", end="")
     for i in range(len(self._data)-1):
       print(round(self._data[i], n), sep=',',end=", ")
     print(round(self._data[i+1],n), end="")
     print("> ")
     return self
 #FUNCTIONS
 # this is for NUMBEr of scalars in vector
  def length(self):
     return(len(self._data))
   
 #this method returns the vector's scalars as a list
  def scalars(self):
     return self._data
 
  def equals(self, other):
     self._data= other._data[:]
     return Vector(self._data)
  def dist(self, other):
     return(self-other).mag()
  def dotProd(self, other):
     return sum([self._data[i]*other._data[i] for i in range(len(self._data))])
 
  def crossProd(X, Y):
     return Vector(X._data[1]*Y._data[2]-X._data[2]*Y._data[1],
                 X._data[2]*Y._data[0]-X._data[0]*Y._data[2],
                 X._data[0]*Y._data[1]-X._data[1]*Y._data[0])
   
  def mag(self):
     from math import sqrt
     return sqrt(sum([i*i for i in self._data]))
 
  def normalize(self):
     m=self.mag()
     self._data=(self/m)._data
     return self
 
  def swap(A,B):
     T=Vector(A)
     A.equals(B)
     B.equals(T)
    
   
  def matrixMult(self,M):
     if self.length() is not len(M):
       exit('Inner dimensions of vectors and matrix NOT equal.')
     W=[0]*len(M[0])
     sum=0
     for col in range(len(M[0])):
         for i in ragne(self.length()):
             sum+=self._data[i]*M[i][col]
         W[col], sum=sum, 0
     return Vector(W)
 
 #OVERLOADED OPERATORS
 
  def __add__(self, other):
     return Vector(*[self._data[i]+other._data[i] for i in range(len(self._data))])
  
  def __sub__(self, other):
     return -other+self

 #Overload in three forms of multiplication: scalar: 2v, v cross w, and matrix mult: v*m
  def __mul__(self, entity):
     if isinstance(entity, (Vector)):
       return self.crossProd(entity)
     if isinstance(entity, (int, float)):
       return Vector(*[i*entity for i in (self._data)])
     if isinstance(entity, (list)):
       return self.matrixMult(entity)
     return NotImplemented
  
  def __rmul__(self, entity):
     return self*entity
  def __truediv__(self, num):
     if num==0:
       return NotImplemented
     return self*(1.0/num)
  def __eq__(self, other):
     return(self._data==other._data[:])
   
  def __ne__(self):
     return Vector(self._data==other._data)
  def __neg__(self):
     return Vector(*[-i for i in self._data])
  def __getitem__(self, index):
     return self._data[index]
  def __setitem__(self, index, num):
     self._data[index]=num
     return self

 #EBD VECTIR CKASS
 
def main():
  A=Vector(1,2,3)
  B=Vector([4,5,6])
  C=Vector((7,8,9))
  
  print('1.', Vector.sortList([C,B,A]))
  print('2.', Vector.sort(A,B,C))
  print('3. Vector A=',A)
  print('4. Vector B=',B)
  print('5. Vector C=',C)
  
  D=Vector(A)
  E=Vector(B)
  D.swap(E)
  print('6.',D,E)
  print('7.',A+B)
  print('8.',(A+B).mag())
  print('9.',A.dist(B))
  print('10.',A.dotProd(B))
  print('11.', A.crossProd(B))
  print('12.',A.normalize().mag())
  print('13.',A-B)
  print('14.',end='')
  Vector.print(A-B,2)
  print('15.',2*A)
  print('16. ',A*2)
  print('17.',A/2, A.length(),A.minVec(B))
  A[0]=100.1234
  print('18.',A)
  print('19.',end='')
  A.print()
  print('20.', end='')
  A.print(3)
  print('21.', B.cost())
  print('22.',B.cost)
  C=Vector(9,8)
  D=Vector(0,1,2,3)
  print('23.', D.equals(C))
  print('24. ', D)
  
if __name__== '__main__': main()
 
   
 