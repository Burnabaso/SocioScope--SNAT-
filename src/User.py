#  Defines the User class with attributes such as user ID, name, list of friends, and other relevant information.
import os
import json
from src.RandomRepeatedFunctionalities import getUserName
UsersDBPath = os.path.join('Data','USersDb.json')


class User:
    #initially the userID will be None to force calling the generateID function
    nextUserID = None
    ####The role of the detectPossibleUserDuplication function####
    # Although every user will get a unique ID so no key error shall occur
    # Yet the user might register a user having the exact same profile data as an existing one
    # This might be a mistake by the user, so a warning will be raised waiting for user confirmation  
    def detectPossibleUserDuplication(name,bio,profilePic):
        with open(UsersDBPath,'r') as file:
            usersData = json.load(file)
            if usersData:
                for user in usersData.values():
                    if user['name'] == name and user['bio'] == bio and user['profile_picture'] == profilePic:
                        print("A possible duplication has been detected a user with same name, bio, and profile picture already exits")
                        print("Do you want to continue registering, ",end="")
                        choice = input("(y/n)?")
                        while choice!="y" and choice!="n":
                            print("Invalid Choice, try again!")
                            choice = input("(y/n)?")
                        if choice == "y":
                            return True
                        else:
                            return False
    #this function will read from the UsersDb.json file and fetch the highest ID in the DB, then sets an new ID incremented by 1
    def generateUserID():
        try:
            with open(UsersDBPath,'r') as file:
                usersData = json.load(file)
                if usersData:
                    latestID = max(int(id) for id in usersData.keys())
                    User.nextUserID = latestID+1
                    return User.nextUserID
                else:
                    return 1
        except FileNotFoundError:
            print("UsersDB file is not found, failed to generate ID!")
    #Class constructor
    def __init__(self,name,bio,profilePic,birthYear,interests=None):
        #To generate a unique ID for each created user
        if User.detectPossibleUserDuplication(name,bio,profilePic):
            if User.nextUserID is None:
                self.userId = User.generateUserID()
            self.name = name
            self.bio = bio
            self.profilePic = profilePic
            self.birthYear = birthYear
            #this makes the interests parameter not mandatory, a new user can ignore writing interests
            self.interests = interests if interests else []
            #ensures no duplicate friendship is stored
            self.friends = set()
            self.addToDb()
            print(f"{self.name} has been registered successfully")
        else:
            print("Your Registration attempt has been cancelled!")
            return
    
    def addFriendByID(self,friendId):
        if friendId in self.friends:
            print(f"A friend of ID {friendId} already exists!")
            return
        result, message = getUserName(friendId)
        if result:
            self.friends.add(friendId)
            print(f"Added user {message} as a friend")
        else:
            print(f"{message}")
            
    def addToDb(self):
        with open(UsersDBPath,'r+') as file:
            userData = json.load(file)
            userData[str(self.userId)]={
                'name': self.name,
                'bio': self.bio,
                'profile_picture': self.profilePic,
                'birthYear': self.birthYear,
                'interests': self.interests,
                #friends is converted to list since JSON don't support sets
                'friends': list(self.friends)
            }
            #moves file pointer to the beginning of the JSON file
            file.seek(0)
            # writes the userData to the JSON file
            json.dump(userData,file,indent=4)

def registerUser(name,bio,profilePic,birthYear,interests):
    #validate that the name entered is a string
    #validate that the username is two words or more
    #validate that bio is a string
    #validate that the profilePic has the extension .jpg or .png in it
    #validate that birth year contains only digits, of length 4 digits and between 1940-2006 as a value
    if type(name) == str and len(name.split(" "))>=2 and type(bio) == str and (".jpg" in profilePic or ".png" in profilePic) and  1939<int(birthYear)<=2006:
        newUser = User(name,bio,profilePic,birthYear,interests)
    #after successful registration of the user, automatically saved to the DB
        return newUser
    elif type(name) != str or len(name.split(" "))<2:
        print("Invalid Name, make sure it is at least of two words and a string")
    elif type(bio) != str:
        print("Invalid bio, make sure it is a string")
    elif ".jpg" not in profilePic and ".png" not in profilePic:
        print("invalid type of profile pic, only jpg or png are accepted!")
    elif not 1939<int(birthYear)<=2006:
        print("Invalid birth year, make sure it is between 1940 and 2006")
    return 

