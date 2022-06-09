class Solution:
    
    probs: List[int]
    size: int

    def __init__(self, w: List[int]):
        self.size = len(w)
        sumW = sum(w)
        self.probs = [0]
        for i in range(self.size):
            addProb = self.probs[i] + (w[i]/sumW)
            self.probs.append(addProb)

    def pickIndex(self) -> int:
        gen = random.random()
        left, right = 0, self.size-1
        # for i in range(self.size):
        #     if self.probs[i]<=r and r<self.probs[i+1]:
        #         return i
        while (left<=right):
            mid = left + (right-left)//2
            if self.probs[mid]<=gen and gen<self.probs[mid+1]:
                return mid
            elif gen<self.probs[mid]:
                right = mid-1
            else:
                left = mid+1
        return (self.size-1)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()