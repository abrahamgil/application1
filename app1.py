import json

data = json.load(open("files/data.json"))
print(data["rain"])

lookup = input("Enter the word you are looking for: ")
print(data[lookup])