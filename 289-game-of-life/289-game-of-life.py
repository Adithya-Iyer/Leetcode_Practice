class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        coords = []
        m, n = len(board), len(board[0])
        def ncnt(x, y):
            cnt = 0
            for i in range(max(0,x-1),min(m-1,x+1)+1):
                for j in range(max(0,y-1),min(n-1,y+1)+1):
                    cnt += board[i][j]
            return cnt
        for i in range(m):
            for j in range(n):
                nbrs = ncnt(i, j)
                if board[i][j]==0:
                    if nbrs==3:
                        coords.append([i,j])
                else:
                    if nbrs<=2 or nbrs>4:
                        coords.append([i,j])
        for x,y in coords:
            board[x][y] ^= 1        