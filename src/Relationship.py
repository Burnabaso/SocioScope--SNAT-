# Manages relationships between users, such as adding or removing friendships or following relationships.
from RandomRepeatedFunctionalities import *

def addFriendByID(userId,friendId):
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

def removeFriendByID(userId,friendId):
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

def checkFriendship(userId,friendId):
    usersData = loadUsers()
    flag = False
    for v in usersData[str(userId)]['friends']:
        if v== str(friendId):
            flag = True
    if flag:
        return True
    else:
        return False

print(checkFriendship(3,2))