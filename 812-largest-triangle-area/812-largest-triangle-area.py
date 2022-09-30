class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0
        n = len(points)
        for i in range(n-2):
            x1, y1 = points[i]
            for j in range(i+1,n-1):
                x2, y2 = points[j]
                for k in range(j+1,n):
                    x3, y3 = points[k]
                    ar = 0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
                    area = max(ar,area)
        return area