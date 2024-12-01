class Solution:
    def maxProfit_approach(self, prices):
        profit_or_loss = []
        for i in range(0, len(prices) - 1):
            for j in range(i+1, len(prices)):
                fluctuation = prices[j] - prices[i]
                profit_or_loss.append(fluctuation)
        if len(prices) <= 1:
            return 0
        elif max(profit_or_loss) < 0:
            return 0
        else:
            return max(profit_or_loss)    
        
    
obj = Solution()
print(obj.maxProfit_approach(prices = [7,1,5,3,6,4]))
print(obj.maxProfit_approach(prices = [7,6,4,3,1]))