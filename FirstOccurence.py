def strStr(haystack, needle):
    for i in range(0, len(haystack)):
        if needle in haystack:
            return i
    else:
        return -1

print(strStr(haystack = "sadbutsad", needle = "sad"))
print(strStr(haystack = "leetcode", needle = "leeto"))