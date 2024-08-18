"""// Implement an algorithm to determine if a string has all unique characters.
// What if you cannot use additional data structures?"""

def isUnique(stringValue):
    for i in range(len(stringValue)):
        for j in range(i+1,len(stringValue)):
            if (stringValue[i] == stringValue[j]):
               return False
    return True

"""// Implement an algorithm to determine if a string has all unique characters.
// You can use additional data structures
def isUnique1(stringValue):
    values = []
    for i in range(len(stringValue)):
        if stringValue[i] in values:
            return False

        values.append(stringValue[i])
    
    return True
"""