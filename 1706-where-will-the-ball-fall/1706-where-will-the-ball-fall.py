class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        if n==1:
            return [-1]
        ball = [j for j in range(n)]
        for i in range(m):
            for posn, b in enumerate(ball):
                if b==-1:
                    continue
                if b==0:
                    if grid[i][b]==-1 or grid[i][b+1]==-1:
                        ball[posn] = -1
                    else:
                        ball[posn] += 1
                elif b==n-1:
                    if grid[i][b]==1 or grid[i][b-1]==1:
                        ball[posn] = -1
                    else:
                        ball[posn] -= 1
                else:
                    if grid[i][b]==1:
                        if grid[i][b+1]==1:
                            ball[posn] += 1
                        else:
                            ball[posn] = -1
                    else:
                        if grid[i][b-1]==-1:
                            ball[posn] -= 1
                        else:
                            ball[posn] = -1
        return ball