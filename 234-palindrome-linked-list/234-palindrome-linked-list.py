# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        numbers = []
        num = 0
        while(True):
            numbers.append(head.val)
            num+=1
            if(head.next==None):
                break
            head = head.next
        #print(numbers)
        for ind in range(num):
            if not (numbers[ind]==numbers[num-1-ind]):
                return False
        return True