class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini, maxp = prices[0], 0
        for i in range(1, len(prices)):
            if(mini>prices[i]):
                mini = prices[i]
            else:
                maxp = max(maxp, (prices[i]-mini))
        return maxp