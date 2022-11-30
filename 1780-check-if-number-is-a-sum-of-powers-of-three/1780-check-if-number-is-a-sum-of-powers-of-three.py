class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        num = n
        for i in reversed(range(1,int(log(n,3))+1)):
            p = int(3**i)
            if num>=p:
                num -= p
            if num<=1:
                return True
        return (False or n==1)