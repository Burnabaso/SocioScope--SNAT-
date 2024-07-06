# This file contains some repeated code that I deemed important to put as functions but they are not a core operation in the program
import os
import json

UsersDBPath = os.path.join('Data','USersDb.json')
IDsDBPath = os.path.join('Data','AvailableIDs.json')
hashTablePath = os.path.join('Data','IDtoMatIndexTable.json')

def ExitMessage():
    print("\nExiting SocioScope...\n")
    exit()
    
def checkChoice(choice,answ1,answ2):
    while choice != answ1 and choice != answ2:
        print("\nInvalid choice, try again!")
        choice = input(f"({answ1}/{answ2})? ")
    return choice
    
def loadUsers():
    with open(UsersDBPath,'r') as file:
        usersData = json.load(file)
    return usersData

def updateUser(userData):
    with open(UsersDBPath,'w') as file:
        file.seek(0)
    # writes the userData to the JSON file
        json.dump(userData,file,indent=4)
        
def updateUsersDB(usersData):
    #moves file pointer to the beginning of the JSON file
    sortedUsersData = dict(sorted(usersData.items(),key=lambda item: int(item[0])))
    with open(UsersDBPath,'w') as file:
        file.seek(0)
    # writes the userData to the JSON file
        json.dump(sortedUsersData,file,indent=4)
                
def loadAvailableIdsListSorted():
    from Algorithms import sortAvailableIDsFile
    with open(IDsDBPath,'r') as file:
        availableIds = json.load(file)
    Idslist = availableIds["availableIds"]
    if len(Idslist)==0:
        return []
    sortAvailableIDsFile(Idslist,0,len(Idslist)-1)
    return Idslist

def updateAvailableIdsList(IdsList):
    with open(IDsDBPath,'w') as file:
        json.dump({"availableIds":IdsList},file,indent=4)
        
def loadHashTable():
    with open(hashTablePath,'r') as file:
        hashData = json.load(file)
    return hashData

def updateHashTable(hashData):
    with open(hashTablePath,'w') as file:
        file.seek(0)
        json.dump(hashData,file,indent=4)
        
def displayUserDataNicely(data):
    for k,v in data.items():
        print(f"\n{k}: {v}")
