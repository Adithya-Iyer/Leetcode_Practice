class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def toeplitz(val, x, y):
            if x>=m or y>=n:
                return True
            return (val==matrix[x][y] and toeplitz(val, x+1, y+1))
        for i in range(m):
            if not toeplitz(matrix[i][0], i+1, 1):
                return False
        for j in range(n):
            if not toeplitz(matrix[0][j], 1, j+1):
                return False
        return True