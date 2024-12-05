class Solution:    
    def plusOne(self, digits):
        def make_a_number(list):
            num_str = ""
            for num in list:
                num_str += str(num)
            return int(num_str)
    
        def make_a_list(number):
            list = []
            for num in str(number):
                list.append(int(num))
            return list
        
        return make_a_list((make_a_number(digits) + 1))
    
obj = Solution()
print(obj.plusOne(digits = [1,2,3]))
print(obj.plusOne(digits = [4,3,2,1]))
print(obj.plusOne(digits = [9]))        