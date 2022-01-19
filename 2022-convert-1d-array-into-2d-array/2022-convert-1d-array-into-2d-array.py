class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        new = []
        l = len(original)
        if (l == m*n):
            for r in range(m):
                new.append(original[r*n: (r+1)*n])
        # else:
        #     new.append([])
        return new