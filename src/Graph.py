# Contains the Graph class for representing the social network using an appropriate data structure (e.g., adjacency list or matrix).
from Relationship import getFriendsList
from RandomRepeatedFunctionalities import loadUsers
import networkx as nx
import matplotlib.pyplot as plt
import os

def getEdges():
    edges = []
    usersData = loadUsers()
    for k in usersData.keys():
        for n in getFriendsList(k):
            edgeSet = []
            edgeSet.append(int(k))
            edgeSet.append(int(n))
            edges.append(tuple(edgeSet))
    
    return edges

class Graph:
    def __init__(self):
        self.numVertices = 0
        self.AM = []

    def buildGraph(self):
        usersData = loadUsers()
        self.numVertices = len(usersData)
        self.AM = [[0]*self.numVertices for _ in range(self.numVertices)]
        edgesList = getEdges()
        
        userIndexMap = {id: idx for idx,id in enumerate(list(usersData.keys()))}
        print(userIndexMap)
        for startV, endV in edgesList:
            print(startV,"=> ",end="")
            print(endV,end="\n")
            if str(startV) in userIndexMap and str(endV) in userIndexMap:
                startIdx = userIndexMap[str(startV)]
                endIdx = userIndexMap[str(endV)]
                self.AM[startIdx][endIdx] = 1
    
    def networkXGraph(self):
        usersIDlist = list(loadUsers().keys())
        edgesList = getEdges()
        G = nx.DiGraph()
        G.add_nodes_from(usersIDlist)
        G.add_edges_from(edgesList)
        return G
    
    def displayGraph(self):
        savePath = os.path.join('Data',"graph.png")
        Gx = self.networkXGraph()
        plt.figure(figsize=(6,6))
        nx.draw_spring(Gx,with_labels=True)
        plt.title("SocioScope Friendship Graph")
        plt.savefig(savePath)
        plt.show()
    
    def displayM(self):
        for row in self.AM:
            print(' '.join(map(str, row)))
g = Graph()
g.displayGraph()

