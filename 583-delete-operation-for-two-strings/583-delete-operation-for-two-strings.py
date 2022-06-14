class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        c = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1]==word2[j-1]:
                    c[i][j] = 1 + c[i-1][j-1]
                else:
                    c[i][j] = max(c[i-1][j], c[i][j-1])
        return m+n-2*c[m][n]