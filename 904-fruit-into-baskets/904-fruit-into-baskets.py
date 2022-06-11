class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        pick = 0
        i = j = 0
        indexDict = {}
        while(j<len(fruits)):
            if(len(indexDict)<=2):
                indexDict[fruits[j]] = j
                j+=1
            if(len(indexDict)>2):
                i = min(indexDict.values()) + 1
                indexDict.pop(fruits[i-1])
            pick = max(pick, j-i)
        return pick