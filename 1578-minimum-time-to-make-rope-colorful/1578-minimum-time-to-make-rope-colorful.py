class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        minTime = 0
        i = 0
        while(i<n-1):
            j = i+1
            while(j<n and colors[i]==colors[j]):
                j += 1
            if j == i+1:
                i += 1
                continue
            temp = neededTime[i:j]
            minTime += sum(temp)-max(temp)
            i = j
        return minTime