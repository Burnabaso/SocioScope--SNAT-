# Manages relationships between users, such as adding or removing friendships or following relationships.
from RandomRepeatedFunctionalities import *
from User import *

def addFriendByID(userId,friendId):
    check1, message1 = User.checkUserAvailability(userId)
    check2, message2 = User.checkUserAvailability(friendId)
    if check1 and check2:
        usersData = loadUsers()
        result, message = getUserName(friendId)
        if str(friendId) in usersData[str(userId)].get('friends',[]):
            print(f"{message} is already friend with User {userId}!")
            return
        if result:
            usersData[str(userId)].get('friends',[]).append(str(friendId))
            print(f"Added user {message} as a friend")
            updateUsersDB(usersData)
        else:
            print(f"{message}")
    elif check1:
        print(message2)
    elif check2:
        print(message1)
    else:
        print(message1)
        print(message2)

def removeFriendByID(userId,friendId):
    check1, message1 = User.checkUserAvailability(userId)
    check2, message2 = User.checkUserAvailability(friendId)
    if check1 and check2:
        usersData = loadUsers()
        result, message = getUserName(friendId)
        if str(friendId) not in usersData[str(userId)].get('friends',[]):
            print(f"{message} is already not a friend with User {userId}!")
            return
        else:
            if result:
                usersData[str(userId)].get('friends',[]).remove(str(friendId))
                print(f"Removed user {message} as a friend")
                updateUsersDB(usersData)
            else:
                print(f"{message}")
    elif check1:
        print(message2)
    elif check2:
        print(message1)
    else:
        print(message1)
        print(message2)

def checkFriendship(userId,friendId):
    check1, message1 = User.checkUserAvailability(userId)
    check2, message2 = User.checkUserAvailability(friendId)
    if check1 and check2: 
        usersData = loadUsers()
        flag = False
        for v in usersData[str(userId)]['friends']:
            if v== str(friendId):
                flag = True
        if flag:
            return True
        else:
            return False
    elif check1:
        print(message2)
    elif check2:
        print(message1)
    else:
        print(message1)
        print(message2)

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
    pass

print(recommendFriendsbyInterests(2))