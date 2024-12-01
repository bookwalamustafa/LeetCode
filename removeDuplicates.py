class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        unique_index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]
            else:
                continue
        return unique_index + 1
    

obj = Solution()
print(obj.removeDuplicates([1,1,2]))
# print(obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))