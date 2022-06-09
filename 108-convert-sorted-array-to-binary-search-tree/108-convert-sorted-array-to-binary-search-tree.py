# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l, r = 0, len(nums)-1
        def getBST(lt: int, rt: int) -> Optional[TreeNode]:
            if (lt>rt):
                return None
            mid = lt + (rt-lt)//2
            return TreeNode(nums[mid], getBST(lt, mid-1), getBST(mid+1, rt))
        return getBST(l, r)