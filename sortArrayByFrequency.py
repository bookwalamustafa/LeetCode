class Solution:
    def frequencySort(self, nums):
        dictionary = {}
        newList = []
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        
        sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: (item[1], -item[0])))
        for item in sorted_dictionary:
            newList.extend([item] * sorted_dictionary[item])
        return newList
        
obj = Solution()
print(obj.frequencySort([1,1,2,2,2,3]))