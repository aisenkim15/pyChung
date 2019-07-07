import json


# filename = 'username.json'
#
# try:
#     with open(filename) as fObj:
#         username = json.load(fObj)
#         # print(username)
# except FileNotFoundError:
#     username = input("What is your name? :")
#     with open(filename, 'w') as fObj:
#         json.dump(username, fObj)
#         print("We will remember you next time you come back... " + username)
# else:
#     print("Welcome back " + username)


def addtoDictionary(userInfo):
    while (True):
        print("Enter \"quit\" as key value when want to stop add key and values")
        newKey = input("Enter the key you want to add..")
        if newKey == "quit":
            break
        newVal = input("Enter the value you want to add..")
        userInfo[newKey] = newVal


def loadFile():
    with open(filename) as fObj:
        userInformation = json.load(fObj)
    return userInformation


filename = 'test.json'
userInfo = {}
with open(filename, 'w') as fObj:
    addtoDictionary(userInfo)
    json.dump(userInfo, fObj)

userInformation = loadFile()

for key, value in userInformation.items():
    print(key + ": " + value)
