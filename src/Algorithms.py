# Includes implementations of graph algorithms like BFS, DFS, and Dijkstra's algorithm for path finding.
import os 
import json
from RandomRepeatedFunctionalities import *
#TODO: Search/sort users by name and yearofbirth

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
            
    return False, f"Data of User {target} can't be retrieved, already deleted or don't exist"

def sortAvailableIDsFile(lst,left,right):
    #using mergeSort algorithm, O(NlgN)
    if left < right:
        mid = (left + right) // 2
        sortAvailableIDsFile(lst, left, mid)
        sortAvailableIDsFile(lst, mid + 1, right)
        merge(lst, left, mid, right)
        
def merge(lst, left,mid,right):
    leftSize = mid - left + 1  
    rightSize = right - mid
    leftLst = [0] * leftSize
    rightList = [0] * rightSize
   
    for i in range(leftSize):
        leftLst[i] = lst[left + i]
    for j in range(rightSize):
        rightList[j] = lst[mid + 1 + j]
    
    indexLeft = 0
    indexRight = 0
    index_merged = left

    while indexLeft < leftSize and indexRight < rightSize:
        if leftLst[indexLeft] <= rightList[indexRight]:
            lst[index_merged] = leftLst[indexLeft]
            indexLeft += 1
        else:
            lst[index_merged] = rightList[indexRight]
            indexRight += 1
        index_merged += 1

    while indexLeft < leftSize:
        lst[index_merged] = leftLst[indexLeft]
        indexLeft += 1
        index_merged += 1

    while indexRight < rightSize:
        lst[index_merged] = rightList[indexRight]
        indexRight += 1
        index_merged += 1