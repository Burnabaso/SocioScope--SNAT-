# Contains the graphical user interface logic for interacting with the social network functionalities.
from User import *
from Relationship import *
from Analysis import * 
from Graph import *
#runs the CLI depending on the user permissions admin//viewer

def runCLI(username,permission):
    print("\nLogging In ...\n")
    print("Welcome",username,"!")
    if permission == "1":
        print("### You are an Admin ###")
        runAdmin()
    else:
        print("### You are a Viewer ###")
        runViewer()
def runAdmin():
    from RandomRepeatedFunctionalities import deleteAllData
    print("\n# Here are the main sections you can Access:")
    adminMenu = """
        1- Users
        2- Graph
        3- DangerZone
        4- Exit (x)
    """
    print(adminMenu)
    choice = input("")
    pass
def runViewer():
    pass