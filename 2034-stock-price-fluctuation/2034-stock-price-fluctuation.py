from heapq import heapify, heappush, heappop

class StockPrice:

    def __init__(self):
        # self.hashmap = {}
        self.times = dict()
        self.vals = dict()
        self.currTS = 0
        self.minheap = []
        heapify(self.minheap)
        self.maxheap = []
        heapify(self.maxheap)

    def update(self, timestamp: int, price: int) -> None:
        # self.hashmap[timestamp] = price
        self.currTS = max(self.currTS, timestamp)
        if timestamp in self.times:
            p = self.times[timestamp]
            self.vals[p] -= 1
            if self.vals[p]==0:
                self.vals.pop(p)
        self.vals[price] = self.vals.get(price, 0) + 1
        self.times[timestamp] = price
        heappush(self.minheap, price)
        heappush(self.maxheap, -price)

    def current(self) -> int:
        # recent = max(self.hashmap.keys())
        # return self.hashmap[recent]
        return self.times[self.currTS]

    def maximum(self) -> int:
        # return max(self.hashmap.values())
        # return max(self.vals.keys())
        p = -self.maxheap[0]
        while(p not in self.vals):
            heappop(self.maxheap)
            p = -self.maxheap[0]
        return p

    def minimum(self) -> int:
        # return min(self.hashmap.values())
        # return min(self.vals.keys())
        p = self.minheap[0]
        while(p not in self.vals):
            heappop(self.minheap)
            p = self.minheap[0]
        return p


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()