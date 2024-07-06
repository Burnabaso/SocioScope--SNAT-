#  Defines the User class with attributes such as user ID, name, list of friends, and other relevant information.

#used to get current year and calculate user age accordingly
import datetime

#import necessary functions from other modules
from RandomRepeatedFunctionalities import loadAvailableIdsListSorted,loadUsers,checkChoice
from Algorithms import *
from Graph import *
class User:
    #initially the userID will be None to force calling the generateID function
    nextUserID = None
    
    ####The role of the detectPossibleUserDuplication function####
    # Although every user will get a unique ID so no key error shall occur
    # Yet the user might register a user having the exact same profile data as an existing one
    # This might be a mistake by the user, so a warning will be raised waiting for user confirmation  
    
    def detectPossibleUserDuplication(name,bio,profilePic):
        # O(N), N being the number of users in the json file
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
            
    #Generate a unique ID for the new User
    def generateUserID():
        # O(N), N being the number of available IDs in the json file
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
        # O(1)
        # Validate if the parameters are of correct format to add to the UsersDB
        if type(name) == str and len(name.split(" "))>=2 and type(bio) == str and (".jpg" in profilePic or ".png" in profilePic) and  1939<int(birthYear)<=2006 and type(interests)==str:
            # check for possible duplication
            if User.detectPossibleUserDuplication(name,bio,profilePic):
                if User.nextUserID is None:
                    # generate an ID for the user
                    self.userId = User.generateUserID()
                    User.nextUserID = None
                self.name = name
                self.bio = bio
                self.profilePic = profilePic
                self.birthYear = birthYear
                self.interests = interests.replace(" ","").lower()
                #initially a user has no friends
                self.friends = []
                # add the user to the Users json file
                self.addToDb()
                print(f"{self.name} has been registered successfully")
            else:
                print("Your Registration attempt has been cancelled!")
                return
            
        # Error handling in case a logical error occured
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
            
    # Check if a user exist
    def checkUserAvailability(id):
        # O(1)
        usersData = loadUsers()
        if str(id) not in usersData.keys():
            return False, f"User of ID({id}) doesn't exist"
        return True, "User found"
    
    # Get friends list of a specific user
    def getFriendsList(id):
        # O(1)
        check, msg = User.checkUserAvailability(id)
        if check:
            usersData = loadUsers()
            return usersData[str(id)]['friends']
        else:
            print(msg)
            
    # Returns a dictionary containing friends list of all users 
    def getAllUsersFriendsList():
        # O(N), N being the number of users in the json file
        friendsDict = {}
        usersData = loadUsers()
        for k, v in usersData.items():
            friendsDict[k] = v["friends"]
        return friendsDict
            
    # return the user age
    def getUserAge(id):
        # O(lgN), N being the length of users in the DB to search for
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
            
    #returns user name
    def getUserName(id):
        # O(1)
        check, message = User.checkUserAvailability(id)
        if check:
            usersData = loadUsers()
            user = usersData.get(str(id))
            return user.get('name')
        else:
            print(message)
            
    # Provides functionality to edit a user profile 
    def updateProfilebyID(id):
        # O(lgN), N being the number of users in the json file to search among
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
            
    # Deletes a user by ID
    def deleteUserByID(id):
        # O(lgN), N being the number of users in the json file to search through
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
            
    # Update Users json file when when user is created
    def addToDb(self):
        # O(1)
        usersData = loadUsers()
        usersData[str(self.userId)]={
            'name': self.name,
            'bio': self.bio,
            'profile_picture': self.profilePic,
            'birthYear': self.birthYear,
            'interests': self.interests,
            #friends is converted to list since JSON don't support sets
            'friends': self.friends
        }
        updateUsersDB(usersData)

