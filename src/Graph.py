# Contains the Graph class for representing the social network using an appropriate adjacency matrix
from src.Relationship import getFriendsList
from src.RandomRepeatedFunctionalities import loadUsers
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt
import os
import heapq

#get edges needed to build the graph
def getEdges():
    # O(N^2), N being the number of users and number of friends of each user
    edges = []
    usersData = loadUsers()
    for k in usersData.keys():
        for n in getFriendsList(k):
            edgeSet = []
            edgeSet.append(int(k))
            edgeSet.append(int(n))
            edges.append(tuple(edgeSet))
    
    return edges

# class Graph Structure
class Graph:
    def __init__(self):
        # O(1)
        usersData = loadUsers()
        self.numVertices = 0
        self.AM = []
        # index maps used to relate the id of the user to its index in the AM
        self.userIndexMap = {id: idx for idx,id in enumerate(list(usersData.keys()))}
        self.indexUserMap = {idx: id for id, idx in self.userIndexMap.items()}

    # builds the graph with the available users and friends data
    def buildGraph(self):
        # O(N^2), N being the number of edges in the list and number of users in the index map
        usersData = loadUsers()
        self.numVertices = len(usersData)
        self.AM = [[0]*self.numVertices for _ in range(self.numVertices)]
        edgesList = getEdges()
        
        for startV, endV in edgesList:
            if str(startV) in self.userIndexMap and str(endV) in self.userIndexMap:
                startIdx = self.userIndexMap[str(startV)]
                endIdx = self.userIndexMap[str(endV)]
                self.AM[startIdx][endIdx] = 1
                
    # Dijkstra algorithm to get shortest path between two users
    def dijkstraAlgorithm(self,user1,user2):
        # O(V^2), V being the number of vertices in the graph
        
        if str(user1) not in self.userIndexMap or str(user2) not in self.userIndexMap:
            return float("inf"), []
        
        startIdx = self.userIndexMap[str(user1)]
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
    
    # Breadth first search algorithm for graph traversal
    def bfs(self, start):
        # O(N^2), N being the number of vertices ad edges in the graph
        # Visited vector to so that a
        # vertex is not visited more than 
        # once Initializing the vector to 
        # false as no vertex is visited at
        # the beginning 
        visited = [False] * self.numVertices
        q = [start]
        lst = []
        # Set source as visited
        visited[start] = True
 
        while q:
            vis = q[0]
            lst.append(vis)
            # # Print current node
            # print(vis, end = ' ')
            q.pop(0)
             
            # For every adjacent vertex to 
            # the current vertex
            for i in range(self.numVertices):
                if (self.AM[vis][i] == 1 and (not visited[i])):
                           
                    # Push the adjacent node 
                    # in the queue
                    q.append(i)
                     
                    # set
                    visited[i] = True
        return lst
    
    # Depth first search algorithm for graph traversal
    def dfs(self, start, visited,lst):
        # O(V^2), V being the number of vertices in the graph
        lst.append(start)
        # # Print current node
        # print(start, end = ' ')
        
 
        # Set current node as visited
        visited[start] = True
 
        # For every node of the graph
        for i in range(self.numVertices):
             
            # If some node is adjacent to the 
            # current node and it has not 
            # already been visited
            if (self.AM[start][i] == 1 and (not visited[i])):
                self.dfs(i, visited,lst)
        return lst
    
    #############################################################
    # These functions are used to implement Kosaraju's algorithm:
    #############################################################
    
    # create a transposed Adjacency matrix 
    def transposeGraph(self):
        # O(V^2), V being the number of vertices in the graph
        transposed = [[self.AM[j][i] for j in range(self.numVertices)] for i in range(self.numVertices)]
        return transposed
    
    # depth first search algorithm when traversing
    def _dfs(self,v,visited,stack):
        # O(V+E), V being the number of vertices and E being the number of edges
        visited.add(v)
        for neighbor in range(self.numVertices):
            if self.AM[v][neighbor] != 0 and neighbor not in visited:
                self._dfs(neighbor, visited, stack)
        stack.append(v)
        
    # traverse the transposed matrix using depth first search algorithm
    def _dfs_transpose(self, v, visited, result):
        # O(V+E), V being the number of vertices and E being the number of edges
        visited.add(v)
        result.append(self.indexUserMap[v])
        for neighbor in range(self.numVertices):
            if self.transposed[v][neighbor] != 0 and neighbor not in visited:
                self._dfs_transpose(neighbor, visited, result)
                
    ############################################################# 
    
    # Uses Kosaraju's Algorithm to find Connected Users
    def findStrongConnectedUsers(self):
        # O(V+E), V being the number of vertices and E being the number of edges
        visited = set()
        stack = []

        # Step 1: Perform DFS and fill the stack in the order of finishing times
        for i in range(self.numVertices):
            if i not in visited:
                self._dfs(i, visited, stack)

        # Step 2: Transpose the graph
        self.transposed = self.transposeGraph()

        # Step 3: Perform DFS on the transposed graph in the order defined by the stack
        visited.clear()
        scc_list = []
        while stack:
            v = stack.pop()
            if v not in visited:
                scc = []
                self._dfs_transpose(v, visited, scc)
                scc_list.append(scc)

        return scc_list
    
    # create a directed graph using networkx library
    def networkXGraph(self):
        # O(N^2), N being the number of users and number of friends of each user
        edgesList = getEdges()
        G = nx.DiGraph()
        G.add_edges_from(edgesList)
        return G
    
    # displays a directed graph using networkx library
    def displayGraph(self):
        # O(N^2), N being the number of users and number of edges
        savePath = os.path.join('Data',"graph.png")
        Gx = self.networkXGraph()
        plt.figure(figsize=(6,6))
        nx.draw_planar(Gx,with_labels=True,font_color='white',node_size=700)
        plt.savefig(savePath)
        plt.show()
    
    def displayAM(self):
        # O(N), N being the number of rows in the AM
        for row in self.AM:
            print(" ".join(map(str, row)))
        print()
    
    def getInDegreeNode(self,node):
        # O(1)
        G=self.networkXGraph()
        return dict(G.in_degree)[node]
    
    def getOutDegreeNode(self,node):
        # O(1)
        G=self.networkXGraph()
        return dict(G.out_degree)[node]
    
    def getDegreeNode(self,node):
        # O(1)
        G=self.networkXGraph()
        return dict(G.degree)[node]
