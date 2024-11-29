class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        new_string = ""
        for char in s_lower:
            if ((ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 48 and ord(char) <= 57)):
                new_string += char
        
        print(new_string)
        reversed_string = new_string[::-1]
        print(reversed_string)
        if reversed_string == new_string:
            return True
        else:
            return False
        
obj = Solution()
print(obj.isPalindrome("0P"))
print(obj.isPalindrome("A man, a plan, a canal: Panama"))
print(obj.isPalindrome(" "))