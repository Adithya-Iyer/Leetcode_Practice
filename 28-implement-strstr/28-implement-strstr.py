class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle==haystack:
            return 0
        h, n = len(haystack), len(needle)
        if n==0:
            return 0
        found = False
        for i in range(h):
            if haystack[i]==needle[0]:
                found = True
                for j in range(1, n):
                    if ((i+j<h) and (haystack[i+j]==needle[j])) and ((i+n-j<h) and (haystack[i+n-j]==needle[n-j])):
                        continue
                    found = False
                    break
                if found:
                    return i
        return -1