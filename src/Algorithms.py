# Includes implementations of graph algorithms like BFS, DFS, and Dijkstra's algorithm for path finding.
from pickle import FALSE
from RandomRepeatedFunctionalities import *

def searchForUserDataByID(target):
    #the search of the target ID is done using binary search algorithm
    #Users are sorted by increasing order of ID by default
    usersData = loadUsers()
    idList = list(map(int,usersData.keys()))
    left = 0
    right = len(idList)-1
    
    while left<=right:
        mid = (left+right)//2
        midId = idList[mid]
        
        if midId == target:
            return True, usersData[str(midId)]
        elif midId < target:
            left = mid +1
        else:
            right = mid-1
            
    return False, f"Data of User {target} can't be retrieved"
