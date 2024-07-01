# This file contains some repeated code that I deemed important to put as functions but they are not a core operation in the program
import os
import json

def ExitMessage():
    print("\n:(")
    print("Exiting SocioScope...\n")
    exit()
    
def checkChoice(choice):
    while choice != "e" and choice != "x":
        print("\nInvalid choice, try again!")
        choice = input("(e/x)? ")
    return True , choice

def getUserName(id):
    UsersDBPath = os.path.join('Data','USersDb.json')
    with open(UsersDBPath,'r') as file:
        usersData = json.load(file)
        user = usersData.get(str(id))
        if user:
            return True, user.get('name')
        else:
            return False , f"User with ID({id}) is not found"