# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower, upper = -(2**31 +1), 2**31
        def validate(node, ll, ul):
            if node==None:
                return True
            v = node.val
            if v<=ll or v>=ul:
                return False
            return validate(node.left, ll, v) and validate(node.right, v, ul)
        return validate(root, lower, upper)