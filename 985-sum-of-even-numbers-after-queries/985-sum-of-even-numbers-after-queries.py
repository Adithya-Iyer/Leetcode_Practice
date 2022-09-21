class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        for n in nums:
            if n%2==0:
                evenSum += n
        answer = []
        for q in queries:
            val, index = q
            if nums[index]%2==0:
                if val%2==0:
                    evenSum += val
                else:
                    evenSum -= nums[index]
            else:
                if val%2==1:
                    evenSum += nums[index] + val
            nums[index] += val
            answer.append(evenSum)
        return answer