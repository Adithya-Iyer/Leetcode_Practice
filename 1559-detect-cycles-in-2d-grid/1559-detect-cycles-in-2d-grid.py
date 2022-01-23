class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        parent = [[[-1,-1] for j in range(n)] for i in range(m)]
        def neighbors(x:int, y:int):# -> List[List[int]]
            ns = []
            if (x>0 and grid[x][y]==grid[x-1][y]):
                ns.append([x-1, y])
            if (x<m-1 and grid[x][y]==grid[x+1][y]):
                ns.append([x+1, y])
            if (y>0 and grid[x][y]==grid[x][y-1]):
                ns.append([x, y-1])
            if (y<n-1 and grid[x][y]==grid[x][y+1]):
                ns.append([x, y+1])
            p = parent[x][y]
            if p in ns:
                ns.remove(p)
            return ns
        def dfs(x:int, y:int):# -> bool:
            ret = False
            visited[x][y] = True
            ns = neighbors(x, y)
            for near in ns:
                i, j = near[0], near[1]
                if visited[i][j]:
                    return True
                parent[i][j] = [x, y]
                ret = dfs(i, j)
                if ret:
                    return True
            return ret
        cycle = False
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                cycle = dfs(i, j)
                if cycle:
                    return True
        return False