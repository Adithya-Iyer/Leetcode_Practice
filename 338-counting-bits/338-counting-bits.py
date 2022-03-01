class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [None for i in range(n+1)]
        bits[0] = 0
        def ones(x):
            ret = 0
            while(x>0):
                ret+=x%2
                x//=2
            return ret
        for i in range(1, n+1):
            if (bits[i]!=None):
                continue
            bits[i] = ones(i)
            j = 2
            while((i*j)<=n):
                bits[i*j]=bits[i]
                j*=2
        return bits