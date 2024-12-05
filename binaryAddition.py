class Solution:    
    def addBinary(self, a: str, b: str):
        def convert_to_decimal(num):
            decimal = 0
            num = num[::-1]
            for i in range(0, len(num)):
                decimal += (int(num[i]) * (2 ** i))
            return decimal
        
        def convert_to_binary(num):
            binary = ""
            while (num >= 1):
                if (num % 2 == 0):
                    binary += "0"
                else:
                    binary += "1"
                num = num // 2
            return binary[::-1]
        
        if (a == "0" and b == "0"):
            return "0"
        else:
            return convert_to_binary((convert_to_decimal(a) + convert_to_decimal(b)))
    
obj = Solution()
print(obj.addBinary('0', '0'))
print(obj.addBinary('11', '1'))
print(obj.addBinary('1010', '1011'))