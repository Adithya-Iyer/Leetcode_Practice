class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        le = len(s)
        lis = list(s)
        for i in range(le//2):
            if(le%(i+1)==0):
                rep = lis[:i+1]
                full = []
                #print(i,le)
                for j in range(int(le/(i+1))):
                    full.extend(rep)
                if (s==''.join(full)):
                    return True
        return False