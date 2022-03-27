class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        t = len(target)
        ret = []
        i = j = 1
        while(i<=t and j<=n):
            if(target[i-1]==j):
                ret.append("Push")
                i+=1
            else:
                ret.extend(['Push','Pop'])
            j+=1
        return ret        