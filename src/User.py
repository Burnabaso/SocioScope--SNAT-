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

        
    
