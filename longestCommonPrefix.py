class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            first_word = strs[0]
            for i in range(0, len(first_word)):
                prefix += first_word[i]
                print("prefix", prefix)
                for string in strs[1:]:
                    if prefix == string[:i+1]:
                        continue
                    else:
                        if len(prefix) <= 0:
                            return ""
                        else:
                            return prefix[:-1]
            return prefix  # Add this line
                        
obj = Solution()
print(obj.longestCommonPrefix(strs = ["", ""]))
# Now, it will correctly print an empty string ""
