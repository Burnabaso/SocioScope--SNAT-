##########################################################################################################
# Manages relationships between users, such as adding or removing friendships or following relationships.#
##########################################################################################################

from src.RandomRepeatedFunctionalities import *
from src.User import *

# Get friends list of a specific user
def getFriendsList(id):
    # O(1)
    check, msg = User.checkUserAvailability(id)
    if check:
        usersData = loadUsers()
        return usersData[str(id)]['friends']
    else:
        print(msg)
        
def getMutualFriends(user1Id,user2Id):
    # O(N^2), N being the number of friends in the friends list
    check1, msg1 = User.checkUserAvailability(user1Id)
    check2, msg2 = User.checkUserAvailability(user2Id)
    if check1 and check2:
        usersData = loadUsers()
        user1FriendsList = usersData[str(user1Id)]['friends']
        user2FriendsList = usersData[str(user2Id)]['friends']
        mutualFriendsList = []
        for m in user1FriendsList:
            if m in user2FriendsList:
                mutualFriendsList.append(m)
        if len(mutualFriendsList)==0:
            print(f"No mutual Friends between {usersData[str(user1Id)]['name']} & {usersData[str(user2Id)]['name']}")
            return
        print(f"Mutual Friends were found between {usersData[str(user1Id)]['name']} & {usersData[str(user2Id)]['name']}")
        return mutualFriendsList
    
    elif check1 != True:
        print(msg1)
    elif check2 != True:
        print(msg2)
    else:
        print(msg1)
        print(msg2)
        
# add a friend to a user by ID
def addFriendByID(userId,friendId):
    # O(1)
    if userId != friendId:
        check1, message1 = User.checkUserAvailability(userId)
        check2, message2 = User.checkUserAvailability(friendId)
        if check1 and check2:
            usersData = loadUsers()
            message = User.getUserName(friendId)
            if str(friendId) in usersData[str(userId)].get('friends',[]):
                print(f"\n{message} is already friend with User {userId}!")
                return
            
            usersData[str(userId)].get('friends',[]).append(str(friendId))
            print(f"\nAdded user {message} as a friend")
            updateUsersDB(usersData)
            
        elif check1:
            print(message2)
        elif check2:
            print(message1)
        else:
            print(message1)
            print(message2)
    else:
        print("\nA user can't be friend with himself")
        return
    
# Remove a friend by ID
def removeFriendByID(userId,friendId):
    # O(1)
    if userId != friendId:
        check1, message1 = User.checkUserAvailability(userId)
        check2, message2 = User.checkUserAvailability(friendId)
        if check1 and check2:
            usersData = loadUsers()
            message = User.getUserName(friendId)
            if str(friendId) not in usersData[str(userId)].get('friends',[]):
                print(f"\n{message} is already not a friend with User {userId}!")
                return
            else:
                usersData[str(userId)].get('friends',[]).remove(str(friendId))
                print(f"\nRemoved user {message} as a friend")
                updateUsersDB(usersData)
                
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
    
# check if two users are friends or not
def checkFriendship(userId,friendId):
    # O(N), N being the number of friends a user has
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
        print("\nA user can't be friend with himself")
        return

