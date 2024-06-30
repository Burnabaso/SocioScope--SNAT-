# Handles user authentication, such as logging in based on hardcoded credentials stored in a file.
# json module provides methods (parsing,reading,writing,...)
import json
import os

def loadLoginData(filePath):
    if not os.path.exists(filePath):
        raise FileNotFoundError("The LoginData file was not found!")
    # with is used for exception handling with files (open and close the file automatically after saving the data in logindata var)
    # r is ensure only reading from the file
    with open(filePath,'r') as file:
        logindata = json.load(file) 
        # convert the json to python object
    return logindata

def authenticateLogin(filePath,username,password):
    
    try:
        loginData = loadLoginData(filePath)
    except FileNotFoundError as FNF:
        return False,str(FNF)
    
    if (username in loginData and loginData[username] == password) and username[-1] == '1':
        return True, "Logging in as an --admin--\n"
    elif (username in loginData and loginData[username] == password) and username[-1] == '2':
        return True, "Logging in as a --viewer--\n"
    else:
        return False, "Invalid username or password!\n"         
        
    