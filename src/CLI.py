# Contains the command line interface logic for interacting with the social network functionalities.

# from Relationship import *
# from Analysis import * 
# from Graph import *
from src.RandomRepeatedFunctionalities import *
from src.User import *

#runs the CLI depending on the user permissions admin//viewer

# TODO: DON'T FORGET TO UNCOMMENT THE DANGER ZONE FUNCTION

##############################################################
################## General welcome cli #######################
##############################################################

def runCLI(username,permission):
    print("\nLogging In ...\n")
    print("### Welcome",username,"! ###")
    if permission == "1":
        print("### You are an Admin ###")
        runAdminMenu()
    else:
        print("### You are a Viewer ###")
        runViewerMenu()
        
###############################################################
####################### Admin Cli #############################
###############################################################
# runs Admin specific cli
def runAdminMenu():
    print("\n# Here are the main sections you can Access:")
    adminMenu = """
        1- Users
        2- Graph
        3- DangerZone
        4- Relations
        x- Exit 
    """
    print(adminMenu)
    try:
        choice = input("Your Choice (1/2/3/4/x): ")
    except KeyboardInterrupt:
        print("\nYou pressed a kill program shortcut")
        ExitMessage()
    choiceValid = checkChoice(choice,"1","2","3","4","x")
    
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
        
###########################################
############# Admin-User-Cli ##############
###########################################       

# runs admin-user cli
def runAdminUserSection():
    print("\n#### Welcome to the User Functionalities Section ####")
    print("As an admin you can:")
    adminUserMenu = """
        1- Add User
        2- Remove User
        3- Update User Profile
        4- Display User Data
        x- Exit
    """
    try:
        choice = input("\n(1/2/3/4/x)?")
    except KeyboardInterrupt:
        print("You pressed a kill program shortcut")
        ExitMessage()
    validChoice = checkChoice(choice,"1","2","3","4","x")
    
    if validChoice == "1":
        #runs user add cli
        runUserAddCli()
            
    elif validChoice == "2":
        # runs user delete cli
        runDeleteUserCli()
    elif validChoice == "3":
        runUpdateUserCli()
    
def runUserAddCli():
    print("\n#### Registering a new User ####")
    print("""
        #################################################
        ############### Instructions ####################
        #################################################
        1) Name must be at least 2 words(e.g: Hala Ammar)
        2) Profile Picture must be .png or .jpg
        3) Birth Year must be between 1940 => 2006
        4) Try to write Interests in the form: "int1,int2,int2" (commas & no spaces)
            """)
    print(""" 
        #############################################################
        ##### Note: ID is generated automatically by SocioScope #####
        #############################################################
        """)
    print("Enter User Info:")
    usrName = input("1) User Name: ")
    usrBio = input("2) Bio: ")
    usrProfilePic = input("3) Profile Picture: ")
    while True:
        try:
            usrBirthYear = int(input("4) Birth Year: "))
            break
        except ValueError:
            print("Birth Year must be strictly integer (2002,1930,...)")
    usrInterests = input("5) Interests(n,m,b,...): ")
    print(f"\nRegistering {usrName} ...")
    usr = User(usrName,usrBio,usrProfilePic,usrBirthYear,usrInterests)
    if usr is not True:
        print("Directing You Back to the MainMenu ...")
        runAdminMenu()
    else:
        print("Directing You back to the User Section ...")
        runAdminUserSection()
        
def runDeleteUserCli():
    # Removing a User
    print("\n#### Removing a User ####")
    print("""
        #################################################
        ############### Instructions ####################
        #################################################
        1) Removing a user must be done by ID number (it is the unique key)
        2) You can search for a user by name and then delete by ID
        3) Once a User is deleted all his friends and data history is gone
            """)
    print(""" 
        ####################################################################################
        ##### Note: ID of deleted user will be saved in a DB to be used with new Users #####
        ####################################################################################
        """)
    
    print("\nEnter user ID to delete (if unknown write 0)",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID = int(input())
            break
        except ValueError:
            print("id must be an integer, try again!")
        except KeyboardInterrupt:
            print("You pressed a kill program shortcut")
            ExitMessage()
    
    usrIdFinal = searchUserCli(usrID,"delete")
    
    # Delete the targeted user by ID
    User.deleteUserByID(usrID)
    # redirect user to the menu
    print("Directing You back to the User Section ...")
    runAdminUserSection()
    
# runs user update info cli
def runUpdateUserCli():
    # Removing a User
    print("\n#### Updating a Users Profile ####")
    print("""
        #################################################
        ############### Instructions ####################
        #################################################
        1) Updating a user's profile must be done by ID number (it is the unique key)
        2) You can search for a user by name and then update by ID
        3) You can update user's bio or interests
        """)
    print(""" 
        ####################################################################################
        ########### Note: Once a User's profile is updated the old version is gone #########
        ####################################################################################
        """)
    
    print("\nEnter user ID to update (if unknown write 0)",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID = int(input())
            break
        except ValueError:
            print("id must be an integer, try again!")
        except KeyboardInterrupt:
            print("You pressed a kill program shortcut")
            ExitMessage()
            
    usrIdFinal = searchUserCli(usrID,"update")
                
    # Delete the targeted user by ID
    User.updateProfilebyID(usrIdFinal)
    # redirect user to the menu
    print("Directing You back to the User Section ...")
    runAdminUserSection()
    
########################################################
################## Search User Cli #####################
########################################################
def searchUserCli(usrID,word):
    # If user input 0 => unknown = Search Sub Menu
    while usrID == 0:        
        print("You can search for users by the following methods:")
        print("""
                1) By Name
                2) By Year of Birth
                """)
        # handle ctr+c keyboard interrupt
        try:
            choice = input("(1/2)?")
        except KeyboardInterrupt:
            print("You pressed a kill program shortcut")
            ExitMessage()
            
        validChoice = checkChoice(choice,"1","2")
        # if 1 was chosen
        if validChoice == "1":
            
            try:
                name = input("Enter name of targeted user: ")
            except KeyboardInterrupt:
                print("You pressed a kill program shortcut")
                ExitMessage()
                
            sortedByName = sortUsersDBbyName()
            data = searchUsersByName(sortedByName,name)
            
            # data returned was empty
            if data is None:
                print(f"{name} was not found")
                print("Directing You back to the User Section ...")
                runAdminUserSection()
            # data was found
            else:
                # display in an appealing way
                displayDictDataNicely(data)
                
        # if 2 was chosen
        else:
            # handle value error (not integer)
            while True:
                try:
                    yob = int(input("Enter year of birth of targeted user: "))
                    break
                except KeyboardInterrupt:
                    print("You pressed a kill program shortcut")
                    ExitMessage()
                except ValueError:
                    print("Year of Birth must be an integer (2002,1950,...)")
                    
            sortedByYOB = sortUsersDBbyYearOfBirth()
            data = searchUsersByYearOfBirth(sortedByYOB,yob)
            
            # data returned was empty
            if data is None:
                print(f"{name} was not found")
                print("Directing You back to the User Section ...")
                runAdminUserSection()
            # data was found
            else:
                # display in an appealing way
                displayDictDataNicely(data)
                
        # Whatever search-way user chose, ID must be used to delete
        print(f"\nEnter user ID to {word} (if unknown write 0)",end="")
        while True:
            try:  
                usrID = int(input())
                break
            except ValueError:
                print("id must be an integer, try again!")
            except KeyboardInterrupt:
                print("You pressed a kill program shortcut")
                ExitMessage()
    return usrID
########################################################
################## Admin-Graph Cli #####################
########################################################    
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
        
def runAdminRelationSection():
    pass

###############################################################
################### Viewer CLi ################################
###############################################################
def runViewerMenu():
    pass
 
