class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        total = mincost = 0
        cost.sort(reverse=True)
        for c in cost:
            total+=1
            if(total%3==0):
                continue
            mincost+=c
        return mincost