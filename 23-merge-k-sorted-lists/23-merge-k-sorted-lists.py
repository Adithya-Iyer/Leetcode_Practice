# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        for node in lists:
            while(node!=None):
                heapq.heappush(minheap, node.val)
                node = node.next
        prev = ListNode(-1)
        head = prev
        for i in range(len(minheap)):
            head.next = ListNode(heapq.heappop(minheap))
            head = head.next
        return prev.next