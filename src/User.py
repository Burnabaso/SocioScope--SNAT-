#  Defines the User class with attributes such as user ID, name, list of friends, and other relevant information.
import os
#used to get current year and calculate user age accordingly
import datetime
from RandomRepeatedFunctionalities import *
from Algorithms import *

UsersDBPath = os.path.join('Data','USersDb.json')
class User:
    #initially the userID will be None to force calling the generateID function
    nextUserID = None
    ####The role of the detectPossibleUserDuplication function####
    # Although every user will get a unique ID so no key error shall occur
    # Yet the user might register a user having the exact same profile data as an existing one
    # This might be a mistake by the user, so a warning will be raised waiting for user confirmation  
    def detectPossibleUserDuplication(name,bio,profilePic):
        flag = False
        usersData = loadUsers()
        if usersData:
            for user in usersData.values():
                if user['name'] == name and user['bio'] == bio and user['profile_picture'] == profilePic:
                    flag=True
            if flag:        
                print("A possible duplication has been detected a user with same name, bio, and profile picture already exits")
                print("Do you want to continue registering, ",end="")
                choice = input("(y/n)?")
                checkChoice(choice,"y","n")
                if choice == "y":
                    return True
                else:
                    return False
            else:
                return True
    #this function will read from the UsersDb.json file and fetch the highest ID in the DB, then sets an new ID incremented by 1
    def generateUserID():
        IdlistData = loadAvailableIdsListSorted()
        if len(IdlistData)==0 :
            try:
                usersData = loadUsers()
                if usersData:
                    latestID = max(int(id) for id in usersData.keys())
                    User.nextUserID = latestID+1
                    return User.nextUserID
                else:
                    return 1
            except FileNotFoundError:
                print("UsersDB file is not found, failed to generate ID!")
        else:
            newId = min(IdlistData)
            IdlistData.remove(newId)
            updateAvailableIdsList(IdlistData)
            return str(newId)
            
    #Class constructor
    def __init__(self,name,bio,profilePic,birthYear,interests):
        # Validate if the parameters are of correct format to add to the UsersDB
        if type(name) == str and len(name.split(" "))>=2 and type(bio) == str and (".jpg" in profilePic or ".png" in profilePic) and  1939<int(birthYear)<=2006 and type(interests)==str:
            if User.detectPossibleUserDuplication(name,bio,profilePic):
                if User.nextUserID is None:
                    self.userId = User.generateUserID()
                    User.nextUserID = None
                self.name = name
                self.bio = bio
                self.profilePic = profilePic
                self.birthYear = birthYear
                #this makes the interests parameter not mandatory, a new user can ignore writing interests
                self.interests = interests.lower()
                #ensures no duplicate friendship is stored
                self.friends = set()
                self.addToDb()
                print(f"{self.name} has been registered successfully")
            else:
                print("Your Registration attempt has been cancelled!")
                return
        elif type(name) != str or len(name.split(" "))<2:
            print("Invalid Name, make sure it is at least of two words and a string")
        elif type(bio) != str:
            print("Invalid bio, make sure it is a string")
        elif ".jpg" not in profilePic and ".png" not in profilePic:
            print("invalid type of profile pic, only jpg or png are accepted!")
        elif not 1939<int(birthYear)<=2006:
            print("Invalid birth year, make sure it is between 1940 and 2006")
        elif type(interests)!=str:
            print("Invalid interests, make sure it is a string")
            
    def checkUserAvailability(id):
        usersData = loadUsers()
        if str(id) not in usersData.keys():
            return False, f"User of ID({id}) doesn't exist"
        return True, "User found"
    
    def getFriendsList(id):
        check, msg = User.checkUserAvailability(id)
        if check:
            usersData = loadUsers()
            return usersData[str(id)]['friends']
        else:
            print(msg)
    def getAllUsersFriendsList():
        friendsDict = {}
        usersData = loadUsers()
        for k, v in usersData.items():
            friendsDict[k] = v["friends"]
        return friendsDict
    def getMutualFriends(user1Id,user2Id):
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
    
    def getUserAge(id):
        check, message = User.checkUserAvailability(id)
        if check: 
            currentYear = datetime.date.today().year
            result, data = searchForUserDataByID(id)
            if result:
                userYear = data['birthYear']
            userAge = currentYear - userYear
            return userAge
        else:
            print(message)
    
    def getUserName(id):
        check, message = User.checkUserAvailability(id)
        if check:
            usersData = loadUsers()
            user = usersData.get(str(id))
            return user.get('name')
        else:
            print(message)
    
    def updateProfilebyID(id):
        check, message = User.checkUserAvailability(id)
        if check:
            result, returnValue = searchForUserDataByID(id)
            if result:
                usersData = loadUsers()
                print(f"What would you like to edit in {returnValue['name']}'s profile?")
                choice = input("Bio or Interests? (b/i) ")
                checkChoice(choice,"b","i")
                if choice == "b":
                    print("Please edit your Bio:")
                    print(returnValue['bio'],"\n")
                    newBio = input()
                    usersData[str(id)]['bio'] = newBio
                    print(f"\n{returnValue['name']}'s bio has been edited successfully!")
                else:
                    print("Please edit your interests")
                    print(returnValue['interests'],"\n")
                    newInterests = input()
                    usersData[str(id)]['interests'] = newInterests
                    print(f"\n{returnValue['name']}'s interests have been edited successfully!")
                    
                updateUsersDB(usersData)
                
            else:
                print(f"{returnValue}")
        else:
            print(message)
            
    def deleteUserByID(id):
        check, message = User.checkUserAvailability(id)
        if check:
            result, returnValue = searchForUserDataByID(id)
            if result:
                print(f"The user of ID({id}) was found with the following data: ")
                displayUserDataNicely(returnValue)
                print("\nWould like to delete this user, ",end="")
                choice = input("(y/n)?")
                checkChoice(choice,"y","n")
                if choice == "y":
                    usersData = loadUsers()
                    del usersData[str(id)]
                    for v in usersData.keys():
                        if str(id) in usersData[v].get('friends',[]):
                            usersData[v].get('friends',[]).remove(str(id))
                    updateUsersDB(usersData)
                    IdList = loadAvailableIdsListSorted()
                    IdList.append(id)
                    updateAvailableIdsList(IdList)
                    print(f"{returnValue["name"]} was removed successfully!")
                else:
                    print("Deletion operation aborted!")
            else:
                print(f"{returnValue}")
        else:
            print(message)
            
    def addToDb(self):
        usersData = loadUsers()
        usersData[str(self.userId)]={
            'name': self.name,
            'bio': self.bio,
            'profile_picture': self.profilePic,
            'birthYear': self.birthYear,
            'interests': self.interests,
            #friends is converted to list since JSON don't support sets
            'friends': list(self.friends)
        }
        updateUsersDB(usersData)