class Solution: 
    def isValid(self, s):
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in brackets:
                # Pop the top element of the stack if it's not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the current closing bracket
                if brackets[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # Stack should be empty for the string to be valid
        return not stack

obj = Solution()
print(obj.isValid("(){}}{")) # False
print(obj.isValid("["))      # False
print(obj.isValid("()[}"))   # False
print(obj.isValid("([)]"))   # False
print(obj.isValid("()"))     # True
print(obj.isValid("()[]"))   # True
print(obj.isValid("(]"))     # False
print(obj.isValid("([])"))   # True