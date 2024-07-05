# Includes implementations of graph algorithms like BFS, DFS, and Dijkstra's algorithm for path finding.
import os 
import json
from RandomRepeatedFunctionalities import *
#TODO: Search/sort users by  and yearofbirth

def sortUsersDBbyName():
    # Built in Timsort algorithm is used to perform the sorting by Names
    # 1 here is the index of the element that contains the user info including the name
    # usersData.items() return such form (id,{userData})
    usersData = loadUsers()
    sortedByName = dict(sorted(usersData.items(), key=lambda item: item[1]['name'].lower()))
    sortedList = list(sortedByName.items())
    return sortedList

def sortUsersDBbyYearOfBirth():
    # Built in Timsort algorithm is used to perform the sorting by year of birth
    # 1 here is the index of the element that contains the user info including the year of birth
    # usersData.items() return such form (id,{userData})
    usersData = loadUsers()
    sortedByYear = dict(sorted(usersData.items(),key=lambda item: item[1]['birthYear']))
    sortedList = list(sortedByYear.items())
    return sortedList

def searchUsersByYearOfBirth(sortedList,year):
    # performs binary search on a list sorted according to year of birth
    left = 0
    right = len(sortedList)-1
    results = []
    while left <= right:
        mid = (left+right)//2
        midYOB = sortedList[mid][1]['birthYear']
        
        if midYOB == year:
            results.append(sortedList[mid])
            # since several users might have same year of birth
            # we check left of the match found and its right
            
            i = mid -1
            #check to its left
            while i>=0 and sortedList[i][1]['birthYear']==year:
                results.append(sortedList[i])
                i-=1
            #check to its right
            i = mid+1
            while i<len(sortedList) and sortedList[i][1]['birthYear']==year:
                results.append(sortedList[i])
                i+=1
            break
        elif midYOB < year:
            left = mid+1
        else:
            right = mid-1
    if results:
        return dict(results)
    else:
        return None
def searchUsersByName(sortedList,name):
    # performs binary search on a list sorted according to names
    left = 0
    right = len(sortedList)-1
    results = []
    while left <= right:
        mid = (left+right)//2
        midName = sortedList[mid][1]['name'].lower()
        
        if midName == name:
            results.append(sortedList[mid])
            # since several users might have same name
            # we check left of the match found and its right
            
            i = mid -1
            #check to its left
            while i>=0 and sortedList[i][1]['name'].lower()==name:
                results.append(sortedList[i])
                i-=1
            #check to its right
            i = mid+1
            while i<len(sortedList) and sortedList[i][1]['name']==name:
                results.append(sortedList[i])
                i+=1
            break
        elif midName < name:
            left = mid+1
        else:
            right = mid-1
    if results:
        return dict(results)
    else:
        return None
                
            
    # usersData = loadUsers()
    # sortedUsersDB = sortUsersDBbyName(usersData)
    # userDict={}
    # for id, info in sortedUsersDB.items():
    #     print(type(info))
    #     if info['name'].lower()==name.lower():
    #         userDict[id]= info
            
    # return userDict if userDict else None

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


