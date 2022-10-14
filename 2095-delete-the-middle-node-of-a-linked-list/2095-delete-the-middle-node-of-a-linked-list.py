# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return None
        if head.next.next==None:
            head.next = None
            return head
        ret = head
        temp = head
        while(temp and temp.next):
            temp = temp.next
            temp = temp.next
            head = head.next
        nxt = head.next
        head.val = nxt.val
        head.next = nxt.next
        return ret