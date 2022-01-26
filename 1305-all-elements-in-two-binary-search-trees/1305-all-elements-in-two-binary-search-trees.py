# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def dm(root):
            if not root:
                return []
            ret = dm(root.right) + [root.val] + dm(root.left)
            return ret
        
        element1 = dm(root1)
        element2 = dm(root2)
        result = []
        while (element1 and element2):
            if (element1[-1]<element2[-1]):
                result.append(element1.pop())
            else:
                result.append(element2.pop())
        
        ret = result + list(reversed(element1 or element2))
        return ret