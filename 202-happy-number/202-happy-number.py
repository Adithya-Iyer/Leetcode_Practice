class Solution:
    def isHappy(self, n: int) -> bool:
        history = {}
        def sumSq(num):
            ss = 0
            while(num>0):
                u = num%10
                ss += u*u
                num = num//10
            return ss
        while(n not in history):
            if n==1:
                return True
            history[n] = True
            n = sumSq(n)
        return False