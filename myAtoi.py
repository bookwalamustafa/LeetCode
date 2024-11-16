def myAtoi(s):
    newNum = ""
    s = s.strip()
    if (s[0].isnumeric()) or (s[0] == "-") or (s[0] == "+"):    
        for i in range(0, len(s)):
            if s[i] == '0':
                continue
            if s[i].isnumeric():
                newNum += s[i]
            else:
                break
    else:
        return 0
    return int(newNum)


print(myAtoi('words and 987'))