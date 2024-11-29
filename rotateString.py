class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        shifts_counter = 0
        while (s != goal):
            if shifts_counter == len(s):
                return False
            else:
                s = s[1:] + s[0]
                shifts_counter += 1
        return True
    
obj = Solution()
print(obj.rotateString("abcde", "abced"))