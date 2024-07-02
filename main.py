from src.LoginAuthentication import *
from src.RandomRepeatedFunctionalities import *
#os will help with cross platform compatibility to handle file path construction in different OS systems
import os
# Getpass will help to hide the password the user is writing at login for security "reasons"
import getpass


        
def main():
    # construct the file path to the login data
    loginDataPath = os.path.join('Data','LoginData.json')
    
    print("""
######################################
####### Welcome to SocioScope ########
######################################
# Your Social Network Analysis Tool ##
######################################
######################################
#        LogIn (e) or Exit (x)       #
#           ##############           #""")
    
    choice = input("(e/x)? ")
    checkChoice(choice,"e","x")
    if choice == "e":    
        username = input("\nUsername: ")
        passcode = getpass.getpass("Password (will be hidden for your security!): ")
        result, message = authenticateLogin(loginDataPath, username,passcode)
        print(message)
        tries = 2
        while result is not True:
            if tries == 0:
                print("No more available tries!")
                ExitMessage() 
            print(f"### Try Again! {tries} chance(s) left!(e)  or exit (x) ###\n")
            
            choice1 = input("(e/x)? ")
            checkChoice(choice1,"e","x")
            if choice1 == "e" and tries!=0:
                username = input("\nUsername: ")
                passcode = getpass.getpass("Password (will be hidden for your security!): ")
                result, message = authenticateLogin(loginDataPath, username,passcode)
                print(message)
                tries-=1     
            elif choice1 == "x" and tries!=0:
                ExitMessage()
                    
        if result:
            #run the CLI
            pass
        
    else:
        ExitMessage()
main()