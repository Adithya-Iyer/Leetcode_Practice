class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) 
        # earliest = target - 1
        # while(earliest!=0 and earliest!=target):
        #     target = earliest
        #     for i in reversed(range(target)):
        #         if nums[i]>=target-i:
        #             earliest = i
        # if earliest==0:
        #     return True
        farthest = -1
        for i in range(target):
            if nums[i]>farthest:
                farthest = nums[i]
            if i==target-1:
                return True
            if farthest==0:
                return False
            farthest -= 1
        return False