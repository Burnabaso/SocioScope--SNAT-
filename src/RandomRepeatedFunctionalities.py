# This file contains some repeated code that I deemed important to put as functions but they are not a core operation in the program
def ExitMessage():
    print("\n:(")
    print("Exiting SocioScope...\n")
    exit()
    
def checkChoice(choice):
    while choice != "e" and choice != "x":
        print("\nInvalid choice, try again!")
        choice = input("(e/x)? ")
    return True , choice