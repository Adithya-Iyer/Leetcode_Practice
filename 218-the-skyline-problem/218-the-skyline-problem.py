class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
            Sweep Line Approach - not original solution
            Link to reference: https://leetcode.com/problems/the-skyline-problem/discuss/2643582
        """
        hashmap = {}
        pqueue, sweepline, ret = [], [], []
        for lft, rgt, ht in buildings:
            heappush(pqueue, [lft, False, ht])
            heappush(pqueue, [rgt, True, ht])
        while pqueue:
            x, dlt, ht = heappop(pqueue)
            if not dlt:
                if not sweepline or ht>-sweepline[0]:
                    if ret and ret[-1][0]==x:
                        ret = ret[:-1]
                    ret.append([x,ht])
                hashmap[ht] = hashmap.get(ht,0) + 1
                heappush(sweepline, -ht)
            else:
                hashmap[ht] = hashmap.get(ht,0) - 1
                if hashmap.get(ht,0)==0 and ht==-sweepline[0]:
                    heappop(sweepline)
                    while sweepline and hashmap.get(-sweepline[0],0)==0:
                        heappop(sweepline)
                    ret.append([x, -sweepline[0] if sweepline else 0])
        return ret