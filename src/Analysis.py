# Provides functions for analyzing network statistics (e.g., average number of friends per user, clustering coefficients) and offering recommendations (e.g., friend recommendations).
from RandomRepeatedFunctionalities import *
from User import *

def recommendFriendsbyAge(id):
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

def recommendFriendsbyInterests(id):
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
    
def recommendFriendsbyMutualFriends(id):
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

def getaverageNumberofFriends():
    usersData = loadUsers()
    numUsers = len(usersData)
    totalFriends = 0
    avg = 0
    for k,v in usersData.items():
        totalFriends += len(v.get('friends',[]))
    if totalFriends > 0:
        avg = round(totalFriends/numUsers,2)
    return avg
        
#TODO: add the netwrok density and cluster coefficient
###### After finishing the graph class
