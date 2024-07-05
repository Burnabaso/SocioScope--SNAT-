# Contains the Graph class for representing the social network using an appropriate data structure (e.g., adjacency list or matrix).
from RandomRepeatedFunctionalities import *
#TODO: start structuring the graph useing adjacency matrix
class Graph:
    def __init__(self):
        usersData = loadUsers()
        self.numUsers = len(usersData)
        self.adjMatrix = [[0]*self.numUsers for _ in range(self.numUsers)]
        
    def addVertex(self):
        self.numUsers = +1
        for row in self.adjMatrix:
            row.append(0)
        self.adjMatrix.append([0]*self.numUsers)
        
    def addEdge(self,usr1,usr2):
        self.adjMatrix[usr1][usr2] = 1
    
    def displayGraph(self):
        if len(self.adjMatrix) == 0:
            print("Graph is empty!")
            return
        for row in self.adjMatrix:
            print(" ".join(map(str,row)))
        