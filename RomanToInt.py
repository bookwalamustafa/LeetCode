def RomanToInt(num):
    dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    # print(len(num))
    for i in range(0, len(num)):
        print(i)
        if ((i+1)!= (len(num))):
            if (dictionary[(num[i])] < dictionary[(num[i+1])]):
                sum += (dictionary[(num[i+1])] - dictionary[(num[i])])
        else:
            sum += (dictionary[(num[i])])
    return sum

print(RomanToInt("IVII"))
# print(RomanToInt("III"))
# print(RomanToInt("LVIII"))
# print(RomanToInt("MCMXCIV"))