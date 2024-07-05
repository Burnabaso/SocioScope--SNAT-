# Manages relationships between users, such as adding or removing friendships or following relationships.
from RandomRepeatedFunctionalities import *
from User import *
from Graph import *

def addFriendByID(userId,friendId):
    if userId != friendId:
        check1, message1 = User.checkUserAvailability(userId)
        check2, message2 = User.checkUserAvailability(friendId)
        if check1 and check2:
            usersData = loadUsers()
            result, message = User.getUserName(friendId)
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
    else:
        print("A user can't be friend with himself")
        return
    
def removeFriendByID(userId,friendId):
    if userId != friendId:
        check1, message1 = User.checkUserAvailability(userId)
        check2, message2 = User.checkUserAvailability(friendId)
        if check1 and check2:
            usersData = loadUsers()
            result, message = User.getUserName(friendId)
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
    else:
        print("A user can't be friend with himself")
        return

def checkFriendship(userId,friendId):
    if userId != friendId:
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
    else:
        print("A user can't be friend with himself")
        return

