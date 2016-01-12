#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     27/05/2014
# Copyright:   (c) Arianna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#for back propogation, just code it
class NeuralNetwork():
    def __init__(self, inputVector, numOfHiddenNodes1,numOfHiddenNodes2, targetVector, fileName=''):
        self.learningRate=0.1
        self.inputVector=inputVector+[-1]
        self.hiddenVector1=[0]*numOfHiddenNodes1 + [-1]
        self.hiddenVector2=[0]*numOfHiddenNodes2 + [-1]
        self.outputVector=[0]*len(targetVector)
        self.targetVector=targetVector
        self.errorVector=[0]*len(targetVector)
        self.sumOfSquaresError=1000
        self.matrix1=self.initializeWeightMatrix(len(self.inputVector),numOfHiddenNodes1)
        self.matrix1=[[0.7,0.2],[.3,.5],[.9,.1],[.4,.6],]
        self.matrix2=self.initializeWeightMatrix(len(self.hiddenVector1),numOfHiddenNodes2)
        self.matrix2=[[0.4,0.1,.6],[.2,.9,.5],[.3,.7,.8],]
        self.matrix3=self.initializeWeightMatrix(len(self.hiddenVector2),len(self.outputVector))
        self.matrix3=[[0.8,0.2],[.5,.4],[.6,.3,],[.1,.7]]
        self.retrieveWeightsFromFile('')#'' means ignore line

        #ONCE DEBUGGED, REMOVE 3 LINES AND 3 LINES ABOVE
        self.printMatrix(self.matrix1,'matrix1')
        self.printMatrix(self.matrix2,'matrix2')
        self.printMatrix(self.matrix3,'matrix3')


    def __repr__(self):
        self.print()
        return ''

    def print(self):
        print('====<NETWORK DATA>========================================')
        print('   1.inputVector =',self.inputVector,'<--added bias= -1')
        self.printMatrix(self.matrix1,'2.matrix1')
        print('    3. hiddenVector1=',self.hiddenVector1,'<--added bias=-1')
        self.printMatrix(self.matrix2,'4. matrix2')
        print('    5. hiddenVector2=',self.hiddenVector2,'<---added bias=-1')
        self.printMatrix(self.matrix3, '4.matrix2')
        print('     7. Output Vector =',self.outputVector,'<--no bias')
        print('     8. Target Vector =',self.targetVector)
        print('     9. Error Vector =',self.errorVector)
        print('     10. sumOfSquaresError =',self.sumOfSquaresError)
        print('     11. LearningRate =', NeuralNetwork.learningRate)
        print('-'*58,'\n')

    def nodeValues(self, V, M):
        assert len(V)==len(M), [len(V), len(M),'Vector and Matrix not compatible for mult']
        VectorOfDotProducts=[]
        for m in range(len(M[0])):
            sum=0
            for v in range(len(V)):
                sum=sum+(V[v]*M[v][m])
            VectorOfDotProducts.append(sum)
        return self.sigmoid(VectorOfDotProducts)

    def sigmoid(self, vector):
        from math import exp
        nodeValueVector=[]
        for n in range(len(vector)):
            nodeValueVector.append(1/(1+exp(-vector[n])))
        return nodeValueVector
    def initializeWeightMatrix(self,row,col):
        assert row>0 and col>0, 'row and col dimensions are negative'
        from random import random
        self.weightMatrix=[[random()*.8+.2 for r in range (col)] for c in range(row)]
    def computerErrorDifferences(self):
      #  from math import *
        assert len(self.targetVector)==len(self.outputVector), 'Target and output = diff lenths'
 #       if self.targetVector!=-1:
#            self.targetVector.append([-1])
        #self.errorVector=[self.targetVector[k]-self.outputVector[k] for k in range(len(self.targetVector))]
        print(self.outputVector[1],"OUTPUT VECT")
        print(self.targetVector[1],"TARGET VECT")
        print(.5*(self.outputVector[1]-self.targetVector[1])**2,"SQUARES ERROR")
        self.sumOfSquaresError=0
        for k in range(len(self.outputVector)):
               self.sumOfSquaresError+=.5*(self.outputVector[k]-self.targetVector[k])**2
               print(self.sumOfSquaresError," ehhh")

##        self.sumOfSquaresError=(.5*(self.outputVector[k]-self.targetVector[k])**2 for k in range(len(self.outputVector)))

##        return self.sumOfSquaresError
    def printMatrix(self, Lst, title='MATRIX'):
        assert type(Lst)==list and type(Lst[0])==list,'Non matrix-type received in printMatrix'
        print('---'+title+":")
        for row in Lst:
            newRow=[]
            for x in row:
                newRow.append(round(x,4))
            for x in newRow:
                print('%11.4f'%x, end='')
            print()
            #dsin()=mlamda
        print('  =============================')
    def feedForward(self):
        self.hiddenVector1=self.nodeValues(self.inputVector,self.matrix1)+[-1]
        self.hiddenVetor2=self.nodeValues(self.hiddenVector1,self.matrix2)+[-1]
        self.outputVector=self.nodeValues(self.hiddenVetor2,self.matrix3)
        self.computerErrorDifferences()
    def backPropogate(self):
        print('Back propogate not finished')
        return
    def storeWeightsIntoFile(self, fileName):
        file1=open(fileName,'wb')
        import pickle
        pickle.dump([self.matrix1,self.matrix2],file1)
        file1.close()
    def verifyFileMatrixDimensions (self,candidateInputWeightmatrix,candidateHiddenWeightMatrix):
        if(len(self.candidateInputWeightMatrix)!=len(InputWeightMatrix) or len(self.candidateInputWeightMatrix[0])!=len(InputWeightMatrix[0])or
        len(self.candidateHiddenWeightMatrix)!= len(HiddenWeightMatrix) or len(self.candidateHiddenWeightMatrix[0])!=len(InputHiddenMatrix[0])):
            print("The input and or hte wight matrices from file are not the size required for this network")
            print('Expected input size:',ln(self.inputVector),'x',numberOfHiddenNodes)
            self.printMatrix(self.candidateInputWeightMatrix, 'candidateInputWeightMatrix')
            print('Expected hidden size:',len(self.hiddenVector1),'x',len(targetVector))
            self.printMatrix(self.candidateHiddenWeightMatrix, 'candidateHiddenWeightMatrix')
            exit()
    def retrieveWeightsFromFile(self, fileName):
        if fileName!='':
            file1=open(fileName,'rb')
            import pickle
            [candidateInputWeightMatrix,candidateHiddenWeightMatrix]=pickle.load(file1)
            file1.close()
            verifyFileMatrixDimensions(self.candidateInputWeightMatrix, self.candidateHiddenWeightMatrix)
            from copy import deepcopy
            self.InputWeightMatrix=deepcopy(candidateInputWeightMatrix)
            self.HiddenWeightMatrix=deepcopoy(candidateHiddenWeightMatrix)

maxEpochsForTraining=1



def main():
    x= NeuralNetwork(inputVector=[1,0,1], numOfHiddenNodes1=2,numOfHiddenNodes2=3,targetVector=[1,0],fileName='')
    print(x.outputVector)
    x.feedForward()
    print(x.outputVector)
    print('sumOfSquaresError (0.2790872737435373)=',x.sumOfSquaresError,'\n')


if __name__ == '__main__':
    main()
