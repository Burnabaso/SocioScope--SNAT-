# Provides functions for analyzing network statistics (e.g., average number of friends per user, clustering coefficients) and offering recommendations (e.g., friend recommendations).
from src.RandomRepeatedFunctionalities import *
from src.User import *
from src.Graph import *

#TODO: Those functions work but let's implement them via graph class
def recommendFriendsByAge(id):
    #recommend possible friends for a user based on age difference
    checkResult, message = User.checkUserAvailability(id)
    if checkResult:
        recommendationDictionary = {}
        usersData = loadUsers()
        userAge = User.getUserAge(id)
        #The acceptable age range to recommend friends is set to 10 years
        acceptableRange = 10
        
        for k,v in usersData.items():
            if k != str(id):
                if k not in usersData[str(id)]['friends']:
                    for item in v:
                        if item =='birthYear':
                            tempAge = User.getUserAge(int(k))
                            name = User.getUserName(int(k))
                            if abs(userAge - tempAge) <= acceptableRange:
                                recommendationDictionary[k] = name
                        
        return recommendationDictionary
    else:
        print(message)

def recommendFriendsByInterests(id):
    checkResult, message = User.checkUserAvailability(id)
    if checkResult:
        usersData = loadUsers()
        recommendationDictionary={}
        userInterestsList = set(usersData[str(id)]['interests'].split(","))
        for k,v in usersData.items():
            if k != str(id):
                if k not in usersData[str(id)]['friends']:
                    for item in v:
                        if item == 'interests':
                            tempInterestList = set(usersData[k]['interests'].split(","))
                            commonInterestsList = userInterestsList.intersection(tempInterestList) 
                            if commonInterestsList:
                                recommendationDictionary[k] = [usersData[k]['name'],list(commonInterestsList)]
                            
        return recommendationDictionary
    else:
        print(message)
    
def recommendFriendsByMutualFriends(id):
    check, message = User.checkUserAvailability(id)
    if check:
        usersData = loadUsers()
        recommendationDictionary = {}
        userfriendslist = User.getFriendsList(id)
       
        for k in usersData.keys():
            if k != str(id) and k in userfriendslist:
                friendFriendsList = User.getFriendsList(int(k))
                for n in friendFriendsList:
                    if n not in userfriendslist and n != str(id):
                        recommendationDictionary[n] = User.getUserName(int(n))
        return recommendationDictionary
    else:
        print(message)
        
# recommend possible users who have the specified user as friend but the latter don't have that user.
def recommendOneSidedFriends(id):
    # O(N^2), N being the the number of users iterating through
    check, message = User.checkUserAvailability(id)
    if check:
        usersData = loadUsers()
        recommendationDictionary = {}
        for k in usersData.keys():
            userfriendslist = User.getFriendsList(k)
            if k != str(id) and str(id) in userfriendslist and k not in User.getFriendsList(id):
                recommendationDictionary[k] = User.getUserName(k)
        return recommendationDictionary
    else:
        print(message)
        
def getAverageNumberOfFriends():
    # O(N), N being the number of users in the json file
    usersData = loadUsers()
    numUsers = len(usersData)
    totalFriends = 0
    avg = 0
    for k,v in usersData.items():
        totalFriends += len(v.get('friends',[]))
    if totalFriends > 0:
        avg = round(totalFriends/numUsers,2)
    return avg

def getNetworkDensity():
    g = Graph()
    g.buildGraph()
    numOfVertices = g.numVertices
    maxNumEdges = numOfVertices*(numOfVertices-1)
    numEdges = len(getEdges())
    networkDensity = numEdges / maxNumEdges
    return round(networkDensity,3)

def getNetworkDensityInPercent():
    return round(getNetworkDensity()*100,3)

def getLocalClusterCoefficient(node):
    node = node - 1
    g = Graph()
    g.buildGraph()
    AM = g.AM
    neighbors = []
    for i in range(len(AM)):
        # check if the target node and the neighboring node have connection
        if AM[node][i] == 1 and i!=node:
            neighbors.append(i)
            
    if len(neighbors)<2:
        return 0.0
    
    actualEdges = 0
    for i in range(len(neighbors)):
        for j in range(i+1,len(neighbors)):
            # check if the neighbor nodes are connected to one another
            if AM[neighbors[i]][neighbors[j]] == 1:
                actualEdges +=1
                
    possibleEdges = len(neighbors)*(len(neighbors)-1)/2
    
    if possibleEdges == 0:
        return 0.0
    
    localCC = actualEdges / possibleEdges
    
    return round(localCC,2)

def getGlobalClusterCoefficient():
    g = Graph()
    g.buildGraph()
    numVertices = g.numVertices
    sumLocalCC = 0
    for node in range(numVertices):
        sumLocalCC += getLocalClusterCoefficient(node)
    globalCC = sumLocalCC / numVertices
    return globalCC
                
    
            
    
    
