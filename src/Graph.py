# Contains the Graph class for representing the social network using an appropriate data structure (e.g., adjacency list or matrix).
from Relationship import getFriendsList
from RandomRepeatedFunctionalities import loadUsers
from User import *
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt
import os
import heapq

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
        usersData = loadUsers()
        self.numVertices = 0
        self.AM = []
        self.userIndexMap = {id: idx for idx,id in enumerate(list(usersData.keys()))}
        self.indexUserMap = {idx: id for id, idx in self.userIndexMap.items()}

        
    def buildGraph(self):
        usersData = loadUsers()
        self.numVertices = len(usersData)
        self.AM = [[0]*self.numVertices for _ in range(self.numVertices)]
        edgesList = getEdges()
        
        for startV, endV in edgesList:
            if str(startV) in self.userIndexMap and str(endV) in self.userIndexMap:
                startIdx = self.userIndexMap[str(startV)]
                endIdx = self.userIndexMap[str(endV)]
                self.AM[startIdx][endIdx] = 1
                
    def dijkstraAlgorithm(self,user1,user2):
        
        if str(user1) not in self.userIndexMap or str(user2) not in self.userIndexMap:
            return float("inf"), []
        
        startIdx = self.userIndexMap[str(user1)]
        print(startIdx)
        endIdx = self.userIndexMap[str(user2)]
        distances = [float("inf")] * self.numVertices
        previous = [None] * self.numVertices
        distances[startIdx] = 0
        
        priorityQueue = [(0, startIdx)]
        heapq.heapify(priorityQueue)
        
        while priorityQueue:
            currentDistance, currentIndex = heapq.heappop(priorityQueue)
            
            if currentDistance > distances[currentIndex]:
                continue
            
            for neighborIndex in range(self.numVertices):
                if self.AM[currentIndex][neighborIndex] != 0:
                    distance = self.AM[currentIndex][neighborIndex]
                    newDistance = currentDistance + distance
                    
                    if newDistance < distances[neighborIndex]:
                        distances[neighborIndex] = newDistance
                        previous[neighborIndex] = currentIndex
                        heapq.heappush(priorityQueue, (newDistance, neighborIndex))
        
        path = []
        currentIndex = endIdx
        while currentIndex is not None:
            path.append(self.indexUserMap[currentIndex])
            currentIndex = previous[currentIndex]
        
        path = path[::-1]  # Reverse the path to get it from start to end
        
        if distances[endIdx] == float("inf"):
            return float("inf"), []
        
        return distances[endIdx], path 
    
    def bfs(self,startUser):
        visited = set()
        queue = deque([startUser-1])  # Convert to 0-based index
        bfsOrder = []
        
        while queue:
            currentVertex = queue.popleft()
            if currentVertex not in visited:
                visited.add(currentVertex)
                bfsOrder.append(currentVertex)
                print(f"Visited: {currentVertex + 1}")  # Debug print
                for neighbor in range(len(self.AM[currentVertex])):
                    if self.AM[currentVertex][neighbor] == 1 and neighbor not in visited:
                        queue.append(neighbor)
                        print(f"Queueing: {neighbor + 1}")  # Debug print

        return [x + 1 for x in bfsOrder]

    def dfs(self,startUser):
        visited = set()
        stack = deque([startUser - 1])
        traversal_order = []

        while stack:
            currentVertex = stack.pop()
            if currentVertex not in visited:
                visited.add(currentVertex)
                traversal_order.append(currentVertex + 1)  # Converting back to 1-indexed

                for neighborIndex in range(len(self.AM[currentVertex]) - 1, -1, -1):
                    if self.AM[currentVertex][neighborIndex] == 1 and neighborIndex not in visited:
                        stack.append(neighborIndex)
                        
        return traversal_order
    
    # These functions are used to implement Kosaraju's algorithm
    def transposeGraph(self):
        # Create a transpose of the adjacency matrix
        transposed = [[self.AM[j][i] for j in range(self.numVertices)] for i in range(self.numVertices)]
        return transposed
    def _dfs(self,v,visited,stack):
        visited.add(v)
        for neighbor in range(self.numVertices):
            if self.AM[v][neighbor] != 0 and neighbor not in visited:
                self._dfs(neighbor, visited, stack)
        stack.append(v)
        
    def _dfs_transpose(self, v, visited, result):
        visited.add(v)
        result.append(self.indexUserMap[v])
        for neighbor in range(self.numVertices):
            if self.transposed[v][neighbor] != 0 and neighbor not in visited:
                self._dfs_transpose(neighbor, visited, result)

    def networkXGraph(self):
        edgesList = getEdges()
        G = nx.DiGraph()
        G.add_edges_from(edgesList)
        return G
    
    def displayGraph(self):
        savePath = os.path.join('Data',"graph.png")
        Gx = self.networkXGraph()
        plt.figure(figsize=(6,6))
        nx.draw_planar(Gx,with_labels=True,font_color='white',node_size=700)
        plt.savefig(savePath)
        plt.show()
    
    def displayAM(self):
        for row in self.AM:
            print(" ".join(map(str, row)))
        print()
    
    def getInDegreeNode(self,node):
        G=self.networkXGraph()
        return dict(G.in_degree)[node]
    
    def getOutDegreeNode(self,node):
        G=self.networkXGraph()
        return dict(G.out_degree)[node]
    
    def getDegreeNode(self,node):
        G=self.networkXGraph()
        return dict(G.degree)[node]
    
        
g = Graph()
g.buildGraph()
distance,path = g.dijkstraAlgorithm(5,6)
print(distance)
print(path)
g.displayAM()
print(g.findStrongConnectedUsers())
g.displayGraph()