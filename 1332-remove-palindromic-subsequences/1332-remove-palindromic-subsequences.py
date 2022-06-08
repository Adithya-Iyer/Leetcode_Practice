class Solution:
    def removePalindromeSub(self, s: str) -> int:
        l = len(s)
        for i in range(l//2):
            if s[i]==s[l-i-1]:
                continue
            return 2
        return 1