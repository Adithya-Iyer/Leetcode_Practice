class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        i, j = 0, len(height)-1
        while(i<j):
            if height[i]<height[j]:
                water = max(water, height[i]*(j-i))
                i+=1
            else:
                water = max(water, height[j]*(j-i))
                j-=1
        return water