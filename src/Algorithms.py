# Includes implementations of graph algorithms like BFS, DFS, and Dijkstra's algorithm for path finding.
from RandomRepeatedFunctionalities import *

# MergeSort Algorithm is used
def sortAvailableIDsFile(lst,left,right):
    #O(NlgN), N being the number of users
    if left < right:
        mid = (left + right) // 2
        sortAvailableIDsFile(lst, left, mid)
        sortAvailableIDsFile(lst, mid + 1, right)
        merge(lst, left, mid, right)
        
def merge(lst, left,mid,right):
    #O(N), N being the number of elements in the lst
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

#Used to be able to search by user name
def sortUsersDBbyName():
    #O(N.MlgN), where M is the average length of user names, and N is the number of users
    usersData = loadUsers()
    # Built in Timsort algorithm (O(NlgN)) is used to perform the sorting by Names
    # usersData.items() return such form (id,{userData})
    # 1 is the index of the element that contains the user info including the name
    # lambda item: item[1]['name'].lower(): O(M), M is the length of the name
    sortedByName = dict(sorted(usersData.items(), key=lambda item: item[1]['name'].lower()))
    sortedList = list(sortedByName.items())
    return sortedList

# Used to be able to search for Users by year of birth
def sortUsersDBbyYearOfBirth():
    #O(N.MlgN), where M is the average length of user names, and N is the number of users
    usersData = loadUsers()
    sortedByYear = dict(sorted(usersData.items(),key=lambda item: item[1]['birthYear']))
    sortedList = list(sortedByYear.items())
    return sortedList

# Binary Search algorithm is used
def searchUsersByYearOfBirth(sortedList,year):
    # O(K), where K is the number of users with the same year of birth
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
    # O(H), where H is the number of users having the specified name
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
# Binary Search Algorithm
def searchForUserDataByID(target):
    #Users are sorted by increasing order of ID by default
    #O(lgN), N being the number of users in the DB
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



