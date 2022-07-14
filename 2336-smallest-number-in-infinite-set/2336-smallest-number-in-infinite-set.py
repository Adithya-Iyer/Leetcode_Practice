class SmallestInfiniteSet:

    def __init__(self):
        self.sis = list(reversed(range(1,1001)))
        self.sans = set()

    def popSmallest(self) -> int:
        sm = self.sis.pop()
        self.sans.add(sm)
        return sm

    def addBack(self, num: int) -> None:
        if num in self.sans:
            self.sis.append(num)
            self.sans.remove(num)
            for i in reversed(range(1, len(self.sis))):
                if self.sis[i]>self.sis[i-1]:
                    self.sis[i], self.sis[i-1] = self.sis[i-1], self.sis[i]
                else:
                    break


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)