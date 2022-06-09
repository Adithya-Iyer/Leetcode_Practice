class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        newDict = {}
        for i in range(len(numbers)):
            #n = numbers[i]
            if numbers[i] in newDict:
                return [newDict[numbers[i]]+1, i+1]
            tminus = target - numbers[i]
            newDict[tminus] = i
        return []