class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minC = prices[0]
        maxP = 0
        for cost in prices:
            if minC>cost:
                minC = cost
            elif minC==cost:
                continue
            else:
                profit = cost - minC
                if profit>maxP:
                    maxP = profit
            #print(cost)
        return maxP