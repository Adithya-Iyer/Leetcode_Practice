class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        hashmap = {0:0}
        i = 0
        n = len(nums)
        while(i<n):
            total += nums[i]
            key = total%k
            if key not in hashmap:
                hashmap[key] = i+1
            elif hashmap[key]<i:
                return True
            i += 1
        return False