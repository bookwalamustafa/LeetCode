class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev           
    
obj = Solution()
print(obj.reverseList([1,2,3,4,5]))
print(obj.reverseList([1,2]))
print(obj.reverseList([]))