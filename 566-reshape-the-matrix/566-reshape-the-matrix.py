class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        # if (m==0):
        #     return mat
        n = len(mat[0])
        # if (n==0):
        #     return mat
        if not (m*n == r*c):
            return mat
        new = [[]]
        i = j = 0
        for row in mat:
            for cell in row:
                new[i].append(cell)
                j+=1
                if (j==c):
                    i, j = i+1, 0
                    if (i<r):
                        new.append([])
        return new        