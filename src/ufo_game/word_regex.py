import re

def buildRegex(wordPattern):
    regex = "^"
    tempPointer = 0
    for i, char in enumerate(wordPattern):
        if char == '_':
            regex += "[a-zA-Z]{1}"
        elif char.isalpha():
            regex += ("[%s%s]{1}" %(char.upper(), char.lower()))
        else:
            print("Error")
            return None

    regex += '$'

    return regex

def buildExcludeRegex(excludedLetters):
    if excludedLetters == None or len(excludedLetters) == 0:
        return "[a-zA-Z]*"
    regex = "^((?!["
    for c in excludedLetters:
        regex += "%s%s" %(c.upper(), c.lower())
    
    regex += "]).)*$"

    return regex
    