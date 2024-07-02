# This file contains some repeated code that I deemed important to put as functions but they are not a core operation in the program
import os
import json

def ExitMessage():
    print("\n:/(")
    print("Exiting SocioScope...\n")
    exit()
    
def checkChoice(choice,answ1,answ2):
    while choice != answ1 and choice != answ2:
        print("\nInvalid choice, try again!")
        choice = input(f"({answ1}/{answ2})? ")

def getUserName(id):
    usersData = loadUsers()
    user = usersData.get(str(id))
    if user:
        return True, user.get('name')
    else:
        return False , f"User with ID({id}) is not found"
    
def loadUsers():
    UsersDBPath = os.path.join('Data','USersDb.json')
    with open(UsersDBPath,'r') as file:
        usersData = json.load(file)
    return usersData