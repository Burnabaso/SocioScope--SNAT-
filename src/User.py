#  Defines the User class with attributes such as user ID, name, list of friends, and other relevant information.
import os
import json
UsersDBPath = os.path.join('Data','USersDb.json')

def getUserName(id):
    with open(UsersDBPath,'r') as file:
        usersData = json.load(file)
        user = usersData.get(str(id))
        if user:
            return True, user.get('name')
        else:
            return False , f"User with ID({id}) is not found"
class User:
    #initially there is 3 registered users, so the first generated id is of value 4 and above
    nextUser = 4
    def __init__(self,name,bio,profilePic,birthYear,interests=None):
        #To generate a unique ID for each created user
        self.userId = User.nextUser
        User.nextUser +=1
        self.name = name
        self.bio = bio
        self.profilePic = profilePic
        self.birthYear = birthYear
        #this makes the interests parameter not mandatory, a new user can ignore writing interests
        self.interests = interests if interests else []
        #ensures no duplicate friendship is stored
        self.friends = set()
    
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
    print(name.split(" "))
    print(len(name.split(" ")))
    print(type(name))
    if type(name) == str and len(name.split(" "))>=2 and type(bio) == str and (".jpg" in profilePic or ".png" in profilePic) and  1939<int(birthYear)<=2006:
        newUser = User(name,bio,profilePic,birthYear,interests)
    #after successful registration of the user, automatically saved to the DB
        newUser.addToDb()
        print(f"{name} has been registered successfully")
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

