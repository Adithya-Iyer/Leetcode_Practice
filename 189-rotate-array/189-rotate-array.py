class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Not original solution
        le = len(nums)
        k%=le
        def partialRotate(lft, rt):
            while lft<rt:
                nums[lft], nums[rt] = nums[rt], nums[lft]
                lft, rt = lft+1, rt-1
        partialRotate(0, le-1)
        partialRotate(0, k-1)
        partialRotate(k, le-1)