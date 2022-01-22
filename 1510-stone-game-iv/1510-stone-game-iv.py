class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mustWin = [False for i in range(n+1)]
        #print(mustWin)
        for j in range(n+1):
            if mustWin[j]:
                continue
            k = 1
            while((k**2 + j)<(n+1)):
                mustWin[(k**2 + j)] = True
                k+=1
        #print(mustWin)
        return mustWin[n]