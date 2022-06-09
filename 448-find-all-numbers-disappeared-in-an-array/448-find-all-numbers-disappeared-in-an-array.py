class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        disNums = []
        count = [0 for i in range(n)]
        for num in nums:
            count[num-1]+=1
        for i in range(n):
            if(count[i]==0):
                disNums.append(i+1)
        return disNums