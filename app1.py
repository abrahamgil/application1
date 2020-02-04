import json

data = json.load(open("files/data.json"))

def lookup(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist. Please try again."

word = input("Enter the word you are looking for: ")

print(lookup(word))