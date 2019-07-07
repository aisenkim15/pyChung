import json

filename = 'numbers.json'
with open(filename) as fObj:
    numbers = json.load(fObj)

print(numbers)
print(type(numbers))