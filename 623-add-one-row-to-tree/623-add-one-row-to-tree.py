# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            temp = TreeNode(val=val, left=root, right=None)
            root = temp
            return root
        oldstack = [root]
        newstack = []
        level = 2
        while(level<depth):
            for node in oldstack:
                if node.left:
                    newstack.append(node.left)
                if node.right:
                    newstack.append(node.right)
            oldstack, newstack = newstack, []
            level += 1
        for node in oldstack:
            lft, rgt = node.left, node.right
            Ltemp = TreeNode(val=val, left=lft, right=None)
            Rtemp = TreeNode(val=val, left=None, right=rgt)
            node.left, node.right = Ltemp, Rtemp
        return root