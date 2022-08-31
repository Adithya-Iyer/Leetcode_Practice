class Solution:
    def romanToInt(self, s: str) -> int:
        conv = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0
        ch = len(s)
        for i in range(ch-1):
            val = conv[s[i]]
            if val<conv[s[i+1]]:
                num -= val
            else:
                num += val
        num += conv[s[-1]]
        return num