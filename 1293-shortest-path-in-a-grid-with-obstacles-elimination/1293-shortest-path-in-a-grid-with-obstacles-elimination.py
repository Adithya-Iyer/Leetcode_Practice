from queue import Queue
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[-1 for j in range(n)] for i in range(m)]
        if m==1 and n==1:
            return 0
        q = Queue()
        q.put([0,0,k,0])
        while(not q.empty()):
            pt = q.get()
            x,y,r,d = pt
            for i,j in ([x-1,y],[x,y-1],[x+1,y],[x,y+1]):
                if i==m-1 and j==n-1:
                    return d+1
                if i>=0 and i<m and j>=0 and j<n and r-grid[i][j]>=0 and visited[i][j]<r-grid[i][j]:
                    q.put([i,j,r-grid[i][j],d+1])
                    visited[i][j] = r-grid[i][j]
        return -1