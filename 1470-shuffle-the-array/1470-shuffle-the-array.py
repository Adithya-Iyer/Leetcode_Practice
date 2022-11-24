class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shfl = []
        for i in range(n):
            shfl.append(nums[i])
            shfl.append(nums[n+i])
        return shfl