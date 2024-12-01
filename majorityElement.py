class Solution:
    def majorityElement(self, nums):
        max_appearance = int(len(nums)/2)
        dictionary = {}
        if max_appearance == 0:
            return nums[0]
        for i in range(0, len(nums)):
            if nums[i] in dictionary:
                dictionary[nums[i]] += 1
            else:
                dictionary[nums[i]] = 1
                
        max_key = max(dictionary, key=dictionary.get)
        max_value = dictionary[max_key]
        
        if max_value > max_appearance:
            return max_key
        else:
            return None
            
           
            
obj = Solution()
print(obj.majorityElement([3,2,3]))
print(obj.majorityElement([2,2,1,1,1,2,2]))