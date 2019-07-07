#
# result = 0
# bools = True
# while(bools):
#     try:
#         num1, num2 = map(int, input("Please enter two \"numbers\"").split())
#         result = num1 + num2
#         bools = False
#     except ValueError:
#         print("You have not entered number. Please enter a number..")
#
#     else:
#         print(result)


# Cats and Dogs
# def openFile(fileName):
#     names=''
#     try:
#         with open(fileName) as fileObj:
#             names = fileObj.readlines()
#     except FileNotFoundError:
#         print("File: " + fileName + " was not found")
#     for name in names:
#         print(name.strip())
#
#
# openFile("dog.txt")


# fileNames = ["cat.txt", "dogs.txt"]
# for file in fileNames:
#     try:
#         with open(file) as f:
#             contents = f.read()
#             print(contents)
#     except FileNotFoundError:
#         pass
#




# def count_words(fileName):
#     try:
#         with open(fileName) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         msg = "sorry, the file " + fileName + "does not exist"
#         print(msg)
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print("The file " + fileName + " has about " + str(num_words) + " words")
#
# filename = "book2.txt"
# count_words(filename)


counter = 0
with open("book2.txt") as file1:
    contents = file1.read()
numCount = contents.count("face")
print(numCount)