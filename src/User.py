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

        
    
