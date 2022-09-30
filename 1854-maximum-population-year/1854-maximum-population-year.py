class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        yearPop = {x:0 for x in range(1950,2051)}
        for b,d in logs:
            for y in range(b,d):
                yearPop[y] += 1
        years = [k for k,_ in sorted(yearPop.items(), key=lambda x: x[1], reverse=True)]
        return years[0]