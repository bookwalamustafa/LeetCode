dict = {"(": 1, ")": 1, "{": 2, "}": 2, "[": 3, "]": 3}

def isValid(s):
    sum = 0
    for i in range(0, len(s)):
        if s[i] == "(" or s[i] == ")":
            sum += 1
            sum += 1
        if s[i] == "{" or s[i] == "}":
            sum += 2
            sum += 2
        if s[i] == "[" or s[i] == "]":
            sum += 3
            sum += 3
    
        
isValid("([])")