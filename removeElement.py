def convertListToString(nums):
    string = ""
    for i in range(0, len(nums)):
        string += (str(nums[i]) + "")
    return string

def convertStringToList(nums):
    list = []
    for i in range(0, len(nums)):
        list.append(nums[i])
    return list

def uniqueElementsCount(nums):
    counter = 0
    for i in range(0, len(nums)):
        if nums[i].isdigit():
            counter += 1
    return counter
            
def removeElement(nums, val):
    newList = []
    val = str(val)
    nums = convertListToString(nums)
    for i in range(0, len(nums)):
        if (val == nums[i]):
            newList = nums.replace(val, '_')
    nums = convertStringToList(newList)
    k = uniqueElementsCount(nums)
    return (k, nums)
        
print(removeElement(nums = [3,2,2,3], val = 3))
print(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))