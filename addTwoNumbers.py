def addTwoNumbers(l1, l2):
    return (add_commas((remove_commas(l1) + remove_commas(l2))))[::-1]
    
def remove_commas(list):
    num = ""
    for i in range(len(list)):
        num = str(list[i]) + num
    return int(num)

def add_commas(sum):
    list_sum = []
    for i in str(sum):
        list_sum.append(int(i))
    return list_sum

            
print(addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))