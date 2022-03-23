class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        new = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                new[i][j] = matrix[j][i]
        return new