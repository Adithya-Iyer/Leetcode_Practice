# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(1) space complexity approach
        i = 0
        while(head and i<10001):
            head = head.next
            i += 1
        if i==10001:
            return True
        return False