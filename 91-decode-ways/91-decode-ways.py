class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        dp = [0 for i in range(l+1)]
        dp[0] = 1
        dp[1] = int(int(s[0])>0)
        for i in range(2, l+1):
            if int(s[i-1:i])>0:
                dp[i] += dp[i-1]
            if int(s[i-2:i])>=10 and int(s[i-2:i])<=26:
                dp[i] += dp[i-2]
        return dp[l]