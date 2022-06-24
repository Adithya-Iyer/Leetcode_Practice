# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if root==None:
            return ret
        q = Queue()
        q.put(root)
        while(not q.empty()):
            n = q.qsize()
            rm = None
            for i in range(n):
                rm = q.get()
                if rm.left:
                    q.put(rm.left)
                if rm.right:
                    q.put(rm.right)
            ret.append(rm.val)
        return ret