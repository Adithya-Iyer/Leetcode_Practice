import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def eucl(pt: List[int]) -> float:
            return pt[0]**2 + pt[1]**2
        maxheap = [(-eucl(points[i]), i) for i in range(k)]
        heapq.heapify(maxheap)
        for j in range(k, len(points)):
            dist = -eucl(points[j])
            if dist > maxheap[0][0]:
                heapq.heappushpop(maxheap, (dist ,j))
        return [points[i] for (_, i) in maxheap]