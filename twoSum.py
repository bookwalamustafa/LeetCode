# First Solution
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []

# Second Solution (Optimized Solution)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if nums[i] in seen:
                return (seen[nums[i]], i)
            seen[complement] = i
