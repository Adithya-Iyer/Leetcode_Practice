class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        def soldiers(row):
            sol = 0
            while(sol<m):
                if(mat[row][sol]==0):
                    break
                sol+=1
            return sol
        strength = {}
        for i in range(n):
            strength[i]=soldiers(i)
        strong = sorted(strength.items(), key=lambda x:x[1])
        ret = []
        j=1
        for row in strong:
            if j>k:
                break
            ret.append(row[0])
            j+=1
        return ret