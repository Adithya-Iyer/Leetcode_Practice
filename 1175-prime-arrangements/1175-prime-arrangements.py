class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        pn, npn = 0, 0
        def isPrime(num):
            if num==1:
                return False
            for i in range(2,int(sqrt(num))+1):
                if num%i==0:
                    return False
            return True
        for j in range(1,n+1):
            if isPrime(j):
                pn += 1
            else:
                npn += 1
        def fact(num):
            f = 1
            for k in range(2,num+1):
                f *= k
            return f
        ret = fact(pn)*fact(npn)
        return (ret%(1000000007))