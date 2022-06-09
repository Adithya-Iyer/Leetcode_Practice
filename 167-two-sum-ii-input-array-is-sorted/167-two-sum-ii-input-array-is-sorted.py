class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        newDict = {}
        for i in range(len(numbers)):
            n = numbers[i]
            if n in newDict:
                return [newDict[n]+1, i+1]
            tminus = target - n
            newDict[tminus] = i
        return []