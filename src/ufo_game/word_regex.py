import re

def buildRegex(wordPattern, excludeLetters = None):
    regex = ""
    tempPointer = 0
    for i, char in enumerate(wordPattern):
        if char == '_':
            regex += "[a-zA-Z]{1}"
        elif char.isalpha():
            regex += ("[%s%s]{1}" %(char.upper(), char.lower()))
        else:
            print("Error")
            return None
    
    for c in excludeLetters:
        regex += f"[^{c.lower()}{c.upper()}]"

    return regex
    