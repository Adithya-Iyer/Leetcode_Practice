class MyHashSet:
    
    buckets = 20011
    hashSet: list()
    
    def __init__(self):
        self.hashSet = [None for i in range(self.buckets)]
    
    def getIndex(self, key: int) -> int:
        return key%self.buckets
    
    def getPosn(self, key: int, index: int) -> int:
        temp = self.hashSet[index]
        if temp:
            for i in range(len(temp)):
                if key==temp[i]:
                    return i
        return -1
    
    def add(self, key: int) -> None:
        index = self.getIndex(key)
        posn = self.getPosn(key, index)
        if posn<0:
            if not self.hashSet[index]:
                self.hashSet[index] = []
            self.hashSet[index].append(key)        

    def remove(self, key: int) -> None:
        index = self.getIndex(key)
        posn = self.getPosn(key, index)
        if not posn<0:
            self.hashSet[index].remove(key)        

    def contains(self, key: int) -> bool:
        index = self.getIndex(key)
        posn = self.getPosn(key, index)
        return (posn>=0)        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)