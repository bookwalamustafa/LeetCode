class Solution:
    def climbStairs(self, n: int) -> int:
        list = [0, 1]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(n):
                list.append((list[-1] + list[-2]))
        return list[-1]
    
obj = Solution()
print(obj.climbingStairs(2))
print(obj.climbingStairs(3))