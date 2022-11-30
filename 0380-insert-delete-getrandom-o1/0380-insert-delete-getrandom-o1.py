class RandomizedSet:

    def __init__(self):
        self.inds = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.inds and self.inds[val]>=0:
            return False
        self.inds[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.inds or self.inds[val]==-1:
            return False
        ind = self.inds[val]
        v = self.vals[-1]
        self.vals[ind] = v
        self.vals.pop()
        self.inds[v] = ind
        self.inds[val] = -1
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()