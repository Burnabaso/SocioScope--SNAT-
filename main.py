#The main file responsible for managing all files in the SNAT
#Just run this file

# Getpass will help to hide the password the user is writing at login for security "reasons"
import getpass

#Import functions for login functionalities
from src.LoginAuthentication import *
#Import exitmessage function to exit the SNAT, and checkChoice to validate user choice
from src.RandomRepeatedFunctionalities import ExitMessage,checkChoice

#Login form SocioScope
def main():
    #Welcome message prompted to the user
    print("""
######################################
####### Welcome to SocioScope ########
######################################
# Your Social Network Analysis Tool ##
######################################
######################################
#        LogIn (e) or Exit (x)       #
#           ##############           #""")
    #choice to login or exit the SNAT
    try:
        choice = input("(e/x)? ")
    except KeyboardInterrupt:
        print("You pressed a kill program shortcut")
        ExitMessage()
        
    validChoice = checkChoice(choice,"e","x")
    
    if validChoice == "e":    
        username = input("\nUsername: ")
        passcode = getpass.getpass("Password (will be hidden for your security!): ")
        #function in the authentication module to validate the user login info
        result, message = authenticateLogin(username,passcode)
        print(message)
        
        # If login info are correct, run CLI with specifying the permission indicator
        if result == True:
            #Import runCli function to run the CLI of SocioScope
            from src.CLI import runCLI
            runCLI(username,username[-1])
            
        else:
            #Give the user 3 tries in total for incorrect login info
            tries = 2
            #the menu that prompts the user to try again if login info incorrect
            while tries > 0 and result is False:
               
                print(f"### Try Again! {tries} chance(s) left!(e)  or exit (x) ###\n")
                
                choice1 = input("(e/x)? ")
                validChoice1 = checkChoice(choice1,"e","x")
                
                if validChoice1 == "e":
                    username = input("\nUsername: ")
                    passcode = getpass.getpass("Password (will be hidden for your security!): ")
                    result, message1 = authenticateLogin(username,passcode)
                    print(message1)
                    tries-=1     
                    
                # If user chose to exit with remaining tries
                else:
                    #function in the randomRepeatedFunctions module to exit the program
                    ExitMessage()
                    
            #in case no more tries
            print("\nNo more available tries!")
            ExitMessage() 
            
    else:
        ExitMessage()
main()