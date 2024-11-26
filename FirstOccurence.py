def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    len_h, len_n = len(haystack), len(needle)

    for i in range(len_h - len_n + 1): 
        if haystack[i:i + len_n] == needle:
            return i

    # return haystack.find(needle)
    return -1

haystack1 = "sadbutsad"
needle1 = "sad"
print(strStr(haystack1, needle1)) 

haystack2 = "leetcode"
needle2 = "leeto"
print(strStr(haystack2, needle2)) 
