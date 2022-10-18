class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        seq = []
        ret = self.countAndSay(n-1)
        i = j = 0
        while j<len(ret):
            while j<len(ret) and ret[i]==ret[j]:
                j += 1
            cnt = j-i
            seq.extend([str(cnt), ret[i]])
            i = j
        return ''.join(seq)