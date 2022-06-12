class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        area = 0
        def dfsS(x: int, y: int) -> int:
            if x<0 or y<0 or x>=m or y>=n or grid[x][y]==0:
                return 0
            a=1
            grid[x][y]=0
            a+=dfsS(x,y-1)
            a+=dfsS(x,y+1)
            a+=dfsS(x-1,y)
            a+=dfsS(x+1,y)
            return a
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    area = max(area, dfsS(i, j))
        return area