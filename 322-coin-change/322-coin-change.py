class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        fewest = [amount+1 for i in range(amount+1)]
        fewest[0] = 0
        coins.sort()
        for i in range(1, amount+1):
            for coin in coins:
                if coin<=i:
                    fewest[i] = min(fewest[i], 1+fewest[i-coin])
        ret = fewest.pop()
        if ret==amount+1:
            return -1
        return ret