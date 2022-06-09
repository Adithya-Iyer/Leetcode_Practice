class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        l = len(s)
        n = l//k
        output = []
        for i in range(n):
            output.append(s[i*k:i*k+k])
        #print (output)
        r = l%k
        if (r==0):
            return output
        end = [s[n*k:]]
        for j in range(k-r):
            end.append(fill)
        output.append(''.join(end))
        return output