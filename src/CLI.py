# Contains the graphical user interface logic for interacting with the social network functionalities.
# from User import *
# from Relationship import *
# from Analysis import * 
# from Graph import *
from src.RandomRepeatedFunctionalities import *

#runs the CLI depending on the user permissions admin//viewer
# TODO: DON'T FORGET TO UNCOMMENT THE DANGER ZONE FUNCTION
def runCLI(username,permission):
    print("\nLogging In ...\n")
    print("### Welcome",username,"! ###")
    if permission == "1":
        print("### You are an Admin ###")
        runAdminMenu()
    else:
        print("### You are a Viewer ###")
        runViewerMenu()
def runAdminMenu():
    print("\n# Here are the main sections you can Access:")
    adminMenu = """
        1- Users
        2- Graph
        3- DangerZone
        x- Exit (x)
    """
    print(adminMenu)
    try:
        choice = input("Your Choice (1/2/3/x): ")
    except KeyboardInterrupt:
        print("\nYou pressed a kill program shortcut")
        ExitMessage()
    choiceValid = checkChoice(choice,"1","2","3","x")
    
    if choiceValid == "1":
        # users section
        runAdminUserSection()
        
    elif choiceValid == "2":
        # graph section 
        runAdminGraphSection()
        
    elif choiceValid == "3":
        # danger zone
        runAdminDangerZone()
    else:
        # exit SocioScope
        ExitMessage()
        
def runAdminUserSection():
    pass

def runAdminGraphSection():
    pass

def runAdminDangerZone():
    print("\nYou Entered the ###Danger Zone###\n")
    print("By Accepting you will *delete* all saved data in SocioScope's Database")
    print("\nYou can confirm deletion (d) <=> Return to MainMenu (r)")
    try:
        choice= input("(d/r)?")
    except KeyboardInterrupt:
        print("\nYou pressed a kill program shortcut")
        ExitMessage()
    validChoice = checkChoice(choice,"d","r")
    
    if validChoice =="d":
        print("\n### Are you sure? there is no undo! ###")
        try:
            choice = input("(y/n)?")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
        validChoice = checkChoice(choice,"y","n")
        if validChoice =="y":
            # deleteAllData()
            print("\nReturning to MainMenu!")
            runAdminMenu()
        else:
            print("\nDeletion cancelled, returning to MainMenu!")
            runAdminMenu()
    else:
        print("\nReturning to MainMenu!")
        runAdminMenu()
    
def runViewerMenu():
    pass
 
