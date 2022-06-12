class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = []
        for c in s:
            if c=='-':
                continue
            chars.append(c.upper())
        n = len(chars)
        p = n//k
        x = n%k
        i = 0
        ret = []
        if(x>0):
            ret.append(''.join(chars[i:i+x]))
            i += x
        for j in range(p):
            ret.append(''.join(chars[i:i+k]))
            i += k
        return '-'.join(ret)