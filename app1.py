import json

data = json.load(open("files/data.json"))

def lookup(word):
    return data[word]

word = input("Enter the word you are looking for: ")

print(lookup(word))