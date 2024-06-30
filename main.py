from src.LoginAuthentication import *
#os will help with cross platform compatibility to handle file path construction in different OS systems
import os
# Getpass will help to hide the password the user is writing at login for security "reasons"
import getpass
def main():
    
    print("""
######################################
####### Welcome to SocioScope ########
######################################
# Your Social Network Analysis Tool ##
######################################
######################################
#               LogIn                #
#           ##############           #""")
    
    username = input("Username: ")
    passcode = getpass.getpass("Password: ")
    
    pass
main()