# Contains the Graph class for representing the social network using an appropriate data structure (e.g., adjacency list or matrix).
from Relationship import getFriendsList
from RandomRepeatedFunctionalities import loadUsers
def getEdges():
   
    edges = []
    usersData = loadUsers()
    for k in usersData.keys():
        for n in getFriendsList(k):
            edgeSet = []
            edgeSet.append(int(k))
            edgeSet.append(int(n))
            edges.append(tuple(edgeSet))
    print(edges)

getEdges()