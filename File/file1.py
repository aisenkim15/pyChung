# fileName = 'pi_digits.txt'

# with open(fileName) as fileObject:
#     for line in fileObject:
#         print(line.rstrip())

# with open(fileName) as fileObject:
#     newList = fileObject.readlines()
#
# for line in newList:
#     print(line.rstrip())


# with open(fileName) as fileObject:
#     newList = fileObject.readlines()
#
# newString = ''
# for lineOfWord in newList:
#     newString += lineOfWord.strip()
# print(newString)
# print(len(newString))


learn_pythonFile = "pi_digits.txt"

"""
#using a for loop 
with open(learn_pythonFile) as fileObject:
    for line in fileObject:
        print(line)
"""

"""
#storing it in a string (printing everything in one line)
newString = ''
with open(learn_pythonFile) as fileObject:
    for line in fileObject:
        newString += line
    print(newString.strip())
"""

"""
newString = ''
with open(learn_pythonFile) as fileObject:
    for line in fileObject:
        newString += line.replace("python", "java")
    print(newString)
"""

"""
with open(learn_pythonFile) as newFileObject:
    for line in newFileObject:
        line = line.replace("python", "C")
        print(line)
"""
# keepGoing = True
# while keepGoing:
#     name = input("Please enter your name to store in to the text file... (enter 'quit' to close the program): ")
#     if name == "quit":
#         keepGoing = False
#     else:
#         with open("newFile.txt", "a") as newObject:
#             newObject.write(name + "\n")
#
# keepGoing = True
# while keepGoing:
#     reason = input("Why do you like programming? --> ")
#     if reason == "quit":
#         keepGoing = False
#         break
#     with open("newFile.txt", "a") as newFile:
#         newFile.write(reason + "\n")


vara, varb = map(int, input("Type two numbers").split())
