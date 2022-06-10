class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        def dfsX(i:int, j:int) -> None:
            if i<0 or j<0 or i>=m or j>=n or board[i][j]=='.':
                return
            board[i][j]='.'
            #dfsX(i-1, j)
            dfsX(i+1, j)
            #dfsX(i, j-1)
            dfsX(i, j+1)
            return
        battleships = 0
        for x in range(m):
            for y in range(n):
                if board[x][y]=='X':
                    battleships+=1
                    dfsX(x,y)
        return battleships