# Contains the command line interface logic for interacting with the social network functionalities.
from src.Relationship import *
from src.Analysis import * 
from src.Graph import *
from src.RandomRepeatedFunctionalities import *
from src.User import *

#runs the CLI depending on the user permissions admin//viewer

##############################################################
################## General welcome cli #######################
##############################################################

def runCLI(username,permission):
    
    print("\n### Welcome",username,"! ###")
    if permission == "1":
        print("\n### You are an Admin ###")
        runAdminMenu()
    else:
        print("\n### You are a Viewer ###")
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
        runCommonGraphSection("a")
        
    elif choiceValid == "3":
        # danger zone
        runAdminDangerZone()
        
    elif choiceValid == "4":
        #relationship zone
        runAdminRelationSection()
    else:
        # exit SocioScope
        ExitMessage()
        
###############################################################
########################## Viewer CLi #########################
###############################################################
# runs viewer specific cli
def runViewerMenu():
    print("\n# Here are the main sections you can Access:")
    adminMenu = """
        1- Users
        2- Graph
        3- Relations
        x- Exit 
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
        runViewerUserSection()
        
    elif choiceValid == "2":
        # graph section 
        runCommonGraphSection("v")
    
    elif choiceValid == "3":
        #relationship zone
        runViewerRelationSection()
    else:
        # exit SocioScope
        ExitMessage()

###################################################
#################### Admin-User-Cli ###############
###################################################      

# runs admin-user cli
def runAdminUserSection():
    print("\n#### Welcome to the User Functionalities Section ####")
    print("As an admin you can:")
    adminUserMenu = """
        1- Add User
        2- Remove User
        3- Update User Profile
        4- Display User Data
        b- Back to Main Menu
        x- Exit
    """
    print(adminUserMenu)
    try:
        choice = input("(1/2/3/4/b/x)? ")
    except KeyboardInterrupt:
        print("\nYou pressed a kill program shortcut")
        ExitMessage()
        
    validChoice = checkChoice(choice,"1","2","3","4","b","x")
    
    if validChoice == "1":
        #runs user add cli
        runUserAddCli()
            
    elif validChoice == "2":
        # runs user delete cli
        runDeleteUserCli()
    elif validChoice == "3":
        # runs user update cli
        runUpdateUserCli()
    elif validChoice == "4":
        # run display user data cli
        runDisplayUserDataCli("a")
        
    elif validChoice == "b":
        runAdminMenu()
    else:
        ExitMessage()
        
############################################
######## User Add cli (Admin Only)##########
############################################

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
     
    User(usrName,usrBio,usrProfilePic,usrBirthYear,usrInterests)
    
    print("\nDirecting You back to the User Section ...")
    runAdminUserSection()
        
############################################
######### User Delete cli (Admin Only) #####
############################################

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
    
    print("\nEnter user ID to delete (if unknown write 0) ",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID = int(input())
            break
        except ValueError:
            print("id must be an integer, try again!")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
    
    usrIdFinal = searchUserCli(usrID,"delete")
    
    # Delete the targeted user by ID
    User.deleteUserByID(usrIdFinal)
    # redirect user to the menu
    print("\nDirecting You back to the User Section ...")
    runAdminUserSection()
    
############################################
######## User Update cli (Admin-Only) ######
############################################

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
    
    print("\nEnter user ID to update (if unknown write 0) ",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID = int(input())
            break
        except ValueError:
            print("id must be an integer, try again!")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
    
    usrIdFinal = searchUserCli(usrID,"update")
                
    # Delete the targeted user by ID
    User.updateProfilebyID(usrIdFinal)
    # redirect user to the menu
    print("\nDirecting You back to the User Section ...")
    runAdminUserSection()
    
############################################
########### User Display cli ###############
############################################

def runDisplayUserDataCli(permission):
    print("\n#### Displaying User Profile ####")
    print("""
        #################################################
        ############### Instructions ####################
        #################################################
        1) Displaying a user's profile must be done by ID number (it is the unique key)
        2) You can search for a user by name and then display by ID
        """)
    
    print("\nEnter user ID to display (if unknown write 0) ",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID = int(input())
            break
        except ValueError:
            print("id must be an integer, try again!")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
            
    usrIdFinal = searchUserCli(usrID,"display")
                
    # Delete the targeted user by ID
    User.displayUserData(usrIdFinal)
    # redirect user to the menu
    print("\nDirecting You back to the User Section ...")
    if permission == "a":
        runAdminUserSection()
    else:
        runViewerUserSection()

########################################################
################## Common-Graph Cli #####################
######################################################## 
   
def runCommonGraphSection(permission=None):
    print("\n####### Welcome to the Graph Functionalities Section ################")
    print("####### Note: the Graph established by SocioScope is Directed #######")
    print("\nAs a user you can:")
    adminUserMenu = """
        1- Find Shortest Path Between Two Users
        2- Traverse the Graph (BFS/DFS)
        3- Find Strong Connected Users
        4- Display Graph
        5- Get Degree of a User (In,Out,Total)
        6- Graph Analysis: Network Density (in %) | Local Cluster Coefficient | Global CC
        b- Back to Main Menu
        x- Exit
    """
    print(adminUserMenu)
    try:
        choice = input("\n(1/2/3/4/5/6/b/x)? ")
    except KeyboardInterrupt:
        print("\nYou pressed a kill program shortcut")
        ExitMessage()
    validChoice = checkChoice(choice,"1","2","3","4","5","6","b","x")
    
    if validChoice == "1":
        #runs short path cli
        runGraphShortPathCli()
            
    elif validChoice == "2":
        # runs graph traverse cli
        runTraverseGraph()
    elif validChoice == "3":
        # runs graph SCC cli
        runSCC()
    elif validChoice == "4":
        runDisplayGraph()
    elif validChoice == "5":
        runGetDegree()
    elif validChoice == "6":
        runGraphAnalysis()
        
    elif validChoice == "b":
        # run the menu of specific user
        if permission == "a":
            runAdminMenu()
        elif permission == "v":
            runViewerMenu()
    else:
        ExitMessage()
    
######################################
########### Short Path cli ###########
######################################

def runGraphShortPathCli():
    print("\n#### Short Path Between Two Users  ####")
    print("""
        #################################################
        ############### Instructions ####################
        #################################################
        1) Short Path Finding must be done by ID number (it is the unique key)
        2) You can search for a user by name and then update by ID
        3) You should provide two user Ids
        """)
    print(""" 
        ####################################################################################
        ########### Note: Path finding algorithm is done by Dijkstra's Algorithm  ##########
        ####################################################################################
        """)
    
    print("\nEnter user 1 ID to findPath (if unknown write 0) ",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID1 = int(input())
            break
        except ValueError:
            print("\nid must be an integer, try again!")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
            
    usrId1Final = searchUserCli(usrID1,"findPath")
    
    print("\nEnter user 2 ID to findPath (if unknown write 0) ",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID2 = int(input())
            break
        except ValueError:
            print("\nid must be an integer, try again!")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
            
    usrId2Final = searchUserCli(usrID2,"findPath")
    # build the graph
    g = Graph()
    g.buildGraph()
    #results of the dijkstra algorithm
    distance,path = g.dijkstraAlgorithm(usrId1Final,usrId2Final)
    if distance==float("inf") and path == []:
        print(f"\nThe distance from user({usrId1Final}) to user({usrId2Final}) doesn't exist")
        print(f"\nThe path from user({usrId1Final}) to user({usrId2Final}) doesn't exist")
    else:
        print(f"\nThe distance from user({usrId1Final}) to user({usrId2Final}) is: {distance}")
        print(f"\nThe path from user({usrId1Final}) to user({usrId2Final}) is: {'=>'.join(path)}")
    # redirect user to the menu
    print("\nDirecting You back to the Graph Section ...")
    runCommonGraphSection()
    
##################################
####### Graph Traverse Cli #######
##################################

def runTraverseGraph():
    print("\n######### Traverse Graph #########")
    print("""
        #################################################
        ############### Instructions ####################
        #################################################
        1) Graph Traversing must be done by ID number (it is the unique key)
        2) You can traverse the graph using BFS or DFS
        """)
    print(""" 
        ####################################################################################
        ########### Note: BFS => Breadth First Search || DFS => Depth First Search #########
        ####################################################################################
        """)
    
    print("\nEnter user ID to traverse (if unknown write 0) ",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID = int(input())
            break
        except ValueError:
            print("id must be an integer, try again!")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
            
    usrIdFinal = searchUserCli(usrID,"traverse")
    
    # choose traverse algorithm
    print("\n### Choose which algorithm to use BFS or DFS")
    
    try:
        choice = input("(b/d)? ")
    except KeyboardInterrupt:
        print("\nYou pressed a kill program shortcut")
        ExitMessage()
        
    validChoice = checkChoice(choice,"b","d")
    
    # build the graph
    g = Graph()
    g.buildGraph()
    
    if validChoice == "b":
        print("\nThe graph traversing using BFS is: ",end="")
        traverse = g.bfs(usrIdFinal)
        traverse = list(map(str, traverse))
        traverse = " => ".join(traverse)
        print(traverse)

    else:
        print("\nThe graph traversing using DFS is: ",end="")
        traverse = g.dfs(usrIdFinal)
        traverse = list(map(str, traverse))
        traverse = " => ".join(traverse)
        print(traverse)
    
    # redirect user to the menu
    print("\nDirecting You back to the Graph Section ...")
    runCommonGraphSection()
    
#####################################
########## SCC Cli ##################
#####################################

def runSCC():
    print("\n######### Strong Connected Users #########")
    print("""
        #################################################
        ############### Instructions ####################
        #################################################
        1) It provides all users who are strong connected
        """)
    print(""" 
        ####################################################################################
        ################# Note: SCC result is done by Kosaraju's Algorithm #################
        ####################################################################################
        """)
    
    g = Graph()
    g.buildGraph()
    
    sccList = g.findStrongConnectedUsers()
    formattedSubLists = [" - ".join(map(str, sublist)) for sublist in sccList]
    formattedScc = " | ".join(formattedSubLists)
    print(f"\nThe SCC nodes(users) are: {formattedScc}")
    
    # redirect user to the menu
    print("\nDirecting You back to the Graph Section ...")
    runCommonGraphSection()
    
#####################################
######### Display Graph Cli #########
#####################################

def runDisplayGraph():
    print("\n######### Display Graph #########")
    print(""" 
        ####################################################################################
        ################# Note: Graph is displayed using networkx library #################
        ####################################################################################
        """)
    
    g = Graph()
    g.buildGraph()
    
    g.displayGraph()
    
    # redirect user to the menu
    print("\nDirecting You back to the Graph Section ...")
    runCommonGraphSection()
    
#####################################
######### Node Degree Cli ###########
#####################################

def runGetDegree():
    print("\n######### Get Degree of a User Node #########")
    print("""
        #################################################
        ############### Instructions ####################
        #################################################
        1) Getting Degree of a User Node must be done by ID number (it is the unique key)
        2) You can search for a user by name and then update by ID
        3) You can get the In|Out|Total degree of a User Node
        """)
    print(""" 
        ####################################################################################
        ########### Note: To get the degree of a user node using networkx builtin methods #########
        ####################################################################################
        """)
    
    print("\nEnter user ID to getDegree (if unknown write 0) ",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID = int(input())
            break
        except ValueError:
            print("id must be an integer, try again!")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
            
    usrIdFinal = searchUserCli(usrID,"getDegree")
    
    print("\nChoose which degree to get In|Out|Total")
    
    try:
        choice = input("(i/o/t)? ")
    except KeyboardInterrupt:
        print("\nYou pressed a kill program shortcut")
        ExitMessage()
    
    validChoice = checkChoice(choice,"i","o","t")
    
    g = Graph()
    g.buildGraph()
    
    if validChoice == "i":
        data = g.getInDegreeNode(usrIdFinal)
        print(f"\nThe -In- degree of the user({usrIdFinal}) is: {data} ",end="")
        
    elif validChoice == "o":
        data = g.getOutDegreeNode(usrIdFinal)
        print(f"\nThe -Out- degree of the user({usrIdFinal}) is: {data} ",end="")
    
    else:
        data = g.getDegreeNode(usrIdFinal)
        print(f"\nThe -Total- degree of the user({usrIdFinal}) is: {data} ",end="")
        
    # redirect user to the menu
    print("\n\nDirecting You back to the Graph Section ...")
    runCommonGraphSection()
        
###########################################
############# Graph - Analysis ############
###########################################
def runGraphAnalysis():
    print("\n######### Graph Analysis Tools #########")
    print("""
        #################################################
        ############### Instructions ####################
        #################################################
        1) You can get meaningful data about the SocioScope network such as:
            a- Network Density
            b- Network Density in %
            c- Local Cluster Coefficient of a certain User (node)
            d- Global Cluster Coefficient of all Users (nodes)
            
        2) You can search for a user by name or year of birth to get LCC
        """)
    print(""" 
        ####################################################################################
        ########### Note: For Local CC you need to specify the id of the user #########
        ####################################################################################
        """)
    
    print("Which graph analysis data you want?")
    print("""
            1- Network Density
            2- Network Density in %
            3- Local Cluster Coefficient of a certain User (node)
            4- Global Cluster Coefficient of all Users (nodes)
          """)
    
    try:  
        choice = input("(1/2/3/4)? ")
        
    except KeyboardInterrupt:
        print("\nYou pressed a kill program shortcut")
        ExitMessage()
        
    validChoice = checkChoice(choice,"1","2","3","4")
    
    if validChoice == "1":
        print("\nThe current network density is: ",getNetworkDensity())
        
    elif validChoice == "2":
        print("\nThe current network density in percent is: ",getNetworkDensityInPercent(),"%")
    
    elif validChoice == "3":
        
        print("\nEnter user ID to getData (if unknown write 0) ",end="")
        # Validate that id is an integer
        while True:
            try:  
                usrID = int(input())
                break
            except ValueError:
                print("id must be an integer, try again!")
            except KeyboardInterrupt:
                print("\nYou pressed a kill program shortcut")
                ExitMessage()
                
        usrIdFinal = searchUserCli(usrID,"traverse")
        
        print(f"\nThe Local Cluster Coefficient of user({usrIdFinal}) is: ",getLocalClusterCoefficient(usrIdFinal))
    else:
        print("\nThe Global Cluster Coefficient in the current network is: ",getGlobalClusterCoefficient())
        
    # redirect user to the menu
    print("\nDirecting You back to the Graph Section ...")
    runCommonGraphSection()

###############################################################
################# Admin-Relationship cli ######################
###############################################################
def runAdminRelationSection():
    print("\n#### Welcome to the Relationship Functionalities Section ####")
    print("####### Note: You can handle all relationships between users #######")
    print("\nAs an admin you can:")
    adminUserMenu = """
        1- Add Friend
        2- Remove Friend
        3- Check Friendship
        4- Get Friend Recommendations by: Age|Interests|Mutual Friends
        5- Get Average Number of Friends in the network
        b- Back to Main Menu
        x- Exit
    """
    print(adminUserMenu)
    try:
        choice = input("\n(1/2/3/4/5/b/x)? ")
    except KeyboardInterrupt:
        print("\nYou pressed a kill program shortcut")
        ExitMessage()
    validChoice = checkChoice(choice,"1","2","3","4","5","b","x")
    
    if validChoice == "1":
        #runs add friend cli
        runAddFriend()
            
    elif validChoice == "2":
        # runs remove friend cli
        runRemoveFriend()
        
    elif validChoice == "3":
        # runs check friendship cli
        runCheckFriendship("a")
        
    elif validChoice == "4":
        #runs friend recommendation cli
        runFriendRecommendation("a")
        
    elif validChoice == "5":
        # runs average friends number cli
        runGetAverageFriends("a")
        
    elif validChoice == "b":
        runAdminMenu()
    else:
        ExitMessage()
    
##################################################
############### Add friend cli ###################
##################################################

def runAddFriend():
    print("\n######### Adding a Friend #########")
    print("""
        #################################################
        ############### Instructions ####################
        #################################################
        1) Adding a friend must be done by ID number (it is the unique key)
        2) You can search for a user by name and then friend by ID
        """)
    
    print("\nEnter user ID to target (if unknown write 0) ",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID1 = int(input())
            break
        except ValueError:
            print("id must be an integer, try again!")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
            
    usrId1Final = searchUserCli(usrID1,"target")
    
    print("\nEnter user ID to becomeFriend (if unknown write 0) ",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID2 = int(input())
            break
        except ValueError:
            print("id must be an integer, try again!")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
            
    usrId2Final = searchUserCli(usrID2,"becomeFriend")

    addFriendByID(usrId1Final,usrId2Final)
    
    print("\nDirecting You back to the Relationship Section ...")
    runAdminRelationSection()

##################################################
############### Remove friend cli ################
##################################################

def runRemoveFriend():
    
    print("\n######### Removing a Friend #########")
    print("""
        #################################################
        ############### Instructions ####################
        #################################################
        1) Removing a friend must be done by ID number (it is the unique key)
        2) You can search for a user by name and then remove friendship by ID
        """)
    
    print("\nEnter user ID to target (if unknown write 0) ",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID1 = int(input())
            break
        except ValueError:
            print("id must be an integer, try again!")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
            
    usrId1Final = searchUserCli(usrID1,"target")
    
    print("\nEnter user ID to removeFriend (if unknown write 0) ",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID2 = int(input())
            break
        except ValueError:
            print("id must be an integer, try again!")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
            
    usrId2Final = searchUserCli(usrID2,"removeFriend")

    removeFriendByID(usrId1Final,usrId2Final)
    
    print("\nDirecting You back to the Relationship Section ...")
    runAdminRelationSection()

##################################################
############### check friendship cli #############
##################################################

def runCheckFriendship(permission):
    
    print("\n######### Check Friendship #########")
    print("""
        #################################################
        ############### Instructions ####################
        #################################################
        1) Checking friendship must be done by ID number (it is the unique key)
        2) You can search for a user by name and then check friendship by ID
        """)
    
    print("\nEnter user ID to target (if unknown write 0) ",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID1 = int(input())
            break
        except ValueError:
            print("id must be an integer, try again!")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
            
    usrId1Final = searchUserCli(usrID1,"target")
    
    print("\nEnter user ID to checkFriend (if unknown write 0) ",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID2 = int(input())
            break
        except ValueError:
            print("id must be an integer, try again!")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
            
    usrId2Final = searchUserCli(usrID2,"checkFriend")

    check = checkFriendship(usrId1Final,usrId2Final)
    
    if check:
        print(f"\nUser({usrId1Final}) is friend with User({usrId2Final})")
    else:
        print(f"\nUser({usrId1Final}) isn't friend with User({usrId2Final})")

    
    print("\nDirecting You back to the Relationship Section ...")
    if permission == "a":
        runAdminRelationSection()
    else:
        runViewerRelationSection()

##################################################
############ Friend Recommendation cli ###########
##################################################

def runFriendRecommendation(permission):
    print("\n######### Friends Recommendations #########")
    print("""
        #################################################
        ############### Instructions ####################
        #################################################
        1) Friend recommendations must be done by ID number (it is the unique key)
        2) You can search for a user by name or YOB and then recommend by ID
        3) You can get recommendations based on: Age | Common Interests | Mutual Friends
        """)
    print(""" 
        ####################################################################################
        ###### Note: This menu only recommends possible friends and don't add them #########
        ####################################################################################
        """)
    
    print("\nEnter user ID to recommendFriends (if unknown write 0) ",end="")
    # Validate that id is an integer
    while True:
        try:  
            usrID = int(input())
            break
        except ValueError:
            print("id must be an integer, try again!")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
            
    usrIdFinal = searchUserCli(usrID,"recommendFriends")
    
    print("\nChoose which recommendation you want: Age | Common Interests | Mutual Friends")
    
    try:
        choice = input("(a/i/f)? ")
    except KeyboardInterrupt:
        print("\nYou pressed a kill program shortcut")
        ExitMessage()
    
    validChoice = checkChoice(choice,"a","i","f")
    
    
    if validChoice == "a":
        data = recommendFriendsByAge(usrIdFinal)
        print(f"\nThe following is the list of recommended users to befriend based on age(range 10 years): ")
        displayRecommendationNicely(data,"a")
        
    elif validChoice == "i":
        data = recommendFriendsByInterests(usrIdFinal)
        print(f"\nThe following is the list of recommended users to befriend based on common interests: ")
        displayRecommendationNicely(data,"i")
    
    else:
        data = recommendFriendsByMutualFriends(usrIdFinal)
        print(f"\nThe following is the list of recommended users to befriend based mutual friends: ")
        displayRecommendationNicely(data,"f")
        
    # redirect user to the menu
    print("\nDirecting You back to the Relationship Section ...")
    if permission == "a":
        runAdminRelationSection()
    else:
        runViewerRelationSection()

##################################################
############ Average Friends cli #################
##################################################

def runGetAverageFriends(permission):
    print("\n######### Average Number of Friends in Network #########")
    
    print("\nThe average number of friends in the entire network of SocioScope is: ",getAverageNumberOfFriends())
    
    # redirect user to the menu
    print("\nDirecting You back to the Relationship Section ...")
    if permission == "a":
        runAdminRelationSection()
    else:
        runViewerRelationSection()

###########################################################################
########################## Viewer-User Section Cli ########################
###########################################################################
def runViewerUserSection():
    print("\n#### Welcome to the User Functionalities Section ####")
    print("As viewer you can:")
    adminUserMenu = """
        1- Search for users
        2- Display User Data
        b- Back to Main Menu
        x- Exit
    """
    print(adminUserMenu)
    try:
        choice = input("\n(1/2/b/x)? ")
    except KeyboardInterrupt:
        print("\nYou pressed a kill program shortcut")
        ExitMessage()
    validChoice = checkChoice(choice,"1","2","b","x")
    
    if validChoice == "1":
        #runs user search cli
        while True:
            try:  
                usrID = int(input())
                break
            except ValueError:
                print("id must be an integer, try again!")
            except KeyboardInterrupt:
                print("\nYou pressed a kill program shortcut")
                ExitMessage()
            
        searchUserCli(usrID,"search")
        # redirect user to the menu
        print("\nDirecting You back to the User Section ...")
        runViewerUserSection()
                    
    elif validChoice == "2":
        # runs user display cli
        runDisplayUserDataCli("v")

    elif validChoice == "b":
        runViewerMenu()
    
    else:
        ExitMessage()

###########################################################################
########################## Viewer-Relations Section Cli ########################
###########################################################################
def runViewerRelationSection():
    print("\n#### Welcome to the Relationship Functionalities Section ####")
    print("####### Note: You can handle all relationships between users #######")
    print("\nAs a viewer you can:")
    adminUserMenu = """
        1- Check Friendship
        2- Get Friend Recommendations by: Age|Interests|Mutual Friends
        3- Get Average Number of Friends in the network
        4- Get Friends list of all users
        b- Back to Main Menu
        x- Exit
    """
    print(adminUserMenu)
    try:
        choice = input("\n(1/2/3/4/b/x)? ")
    except KeyboardInterrupt:
        print("\nYou pressed a kill program shortcut")
        ExitMessage()
    validChoice = checkChoice(choice,"1","2","3","4","b","x")
    
    if validChoice == "1":
         # runs check friendship cli
        runCheckFriendship("v")
            
    elif validChoice == "2":
        #runs friend recommendation cli
        runFriendRecommendation("v")
        
    elif validChoice == "3":
        # runs average number of friends cli
        runGetAverageFriends("v")
        
    elif validChoice == "4":
        #runs get friend list cli
        runFriendList()
        
    elif validChoice == "b":
        runViewerMenu()
    else:
        ExitMessage()
        
##############################################
########### Get user friend list #############
##############################################

def runFriendList():
    print("\n######### Friends List of all Users #########")
    
    print("\nThe list of friends in the entire network of SocioScope is: ")
    data = User.getAllUsersFriendsList()
    displayDictDataNicely(data)
    
    # redirect user to the menu
    print("\nDirecting You back to the Relationship Section ...")
    runViewerRelationSection()
    
####################################################################
###################### DangerZone Cli ##############################
####################################################################

def runAdminDangerZone():
    print("\nYou Entered the ###Danger Zone###\n")
    print("By Accepting you will *delete* all saved data in SocioScope's Database")
    print("\nYou can confirm deletion (d) <=> Return to MainMenu (r)")
    try:
        choice= input("(d/r)? ")
    except KeyboardInterrupt:
        print("\nYou pressed a kill program shortcut")
        ExitMessage()
    validChoice = checkChoice(choice,"d","r")
    
    if validChoice =="d":
        print("\n### Are you sure? there is no undo! ###")
        try:
            choice = input("(y/n)? ")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
        validChoice = checkChoice(choice,"y","n")
        if validChoice =="y":
            deleteAllData()
            print("\nReturning to MainMenu!")
            runAdminMenu()
        else:
            print("\nDeletion cancelled, returning to MainMenu!")
            runAdminMenu()
    else:
        print("\nReturning to MainMenu ...")
        runAdminMenu()
        
########################################################
################## Search User Cli #####################
########################################################

def searchUserCli(usrID,word):
    # If user input 0 => unknown = Search Sub Menu
    while usrID == 0:        
        print("\nYou can search for users by the following methods:")
        print("""
                1) By Name
                2) By Year of Birth
                """)
        # handle ctr+c keyboard interrupt
        try:
            choice = input("(1/2)? ")
        except KeyboardInterrupt:
            print("\nYou pressed a kill program shortcut")
            ExitMessage()
            
        validChoice = checkChoice(choice,"1","2")
        # if 1 was chosen
        if validChoice == "1":
            
            try:
                name = input("Enter name of targeted user: ")
            except KeyboardInterrupt:
                print("\nYou pressed a kill program shortcut")
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
                searchResult(data)
                
        # if 2 was chosen
        else:
            # handle value error (not integer)
            while True:
                try:
                    yob = int(input("\nEnter year of birth of targeted user: "))
                    break
                except KeyboardInterrupt:
                    print("\nYou pressed a kill program shortcut")
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
                searchResult(data)
                
        # Whatever search-way user chose, ID must be used to delete
        print(f"\nEnter user ID to {word} (if unknown write 0) ",end="")
        while True:
            try:  
                usrIDfinal = int(input())
                break
            except ValueError:
                print("id must be an integer, try again!")
            except KeyboardInterrupt:
                print("\nYou pressed a kill program shortcut")
                ExitMessage()
        if usrIDfinal == 0:
            searchUserCli()
        else:
            return usrIDfinal
    return usrID