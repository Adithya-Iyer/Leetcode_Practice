class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for n in nums:
            if n<0:
                neg.append(n)
            else:
                pos.append(n)
        for i in range(len(pos)):
            nums[2*i] = pos[i]
            nums[2*i + 1] = neg[i]
        return nums