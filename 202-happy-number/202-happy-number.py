class Solution:
    def isHappy(self, n: int) -> bool:
        # history = {}
        hist = set()
        def sumSq(num):
            ss = 0
            while(num>0):
                u = num%10
                ss += u*u
                num = num//10
            return ss
        # while(n not in history):
        while(n not in hist):
            if n==1:
                return True
            # history[n] = True
            hist.add(n)
            n = sumSq(n)
        return False