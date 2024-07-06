# Handles user authentication, such as logging in based on hardcoded credentials stored in a file.
# json module provides methods (parsing,reading,writing,...)
import json
import os

# loads the loginData in the json file
def loadLoginData():
    # O(1)
    # construct the file path to the login data
    loginDataPath = os.path.join('Data','LoginData.json')
    if not os.path.exists(loginDataPath):
        raise FileNotFoundError("The LoginData file was not found!")
    # with is used for exception handling with files (open and close the file automatically after saving the data in login data var)
    # r is ensure only reading from the file
    with open(loginDataPath,'r') as file:
        loginData = json.load(file) 
        # convert the json to python object
    return loginData

# validates if the login info entered by user is valid
def authenticateLogin(username,password):
    # O(1)
    try:
        loginData = loadLoginData()
    except FileNotFoundError as FNF:
        return False,str(FNF)
    
    if (username in loginData and loginData[username] == password) and username[-1] == '1':
        return True, "Logging in as an --admin--\n"
    elif (username in loginData and loginData[username] == password) and username[-1] == '2':
        return True, "Logging in as a --viewer--\n"
    else:
        return False, "Invalid username or password!\n"         
        
    