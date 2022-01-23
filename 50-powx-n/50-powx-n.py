class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if (x==1):
            return 1
        if (x==-1):
            if (n%2==0):
                return 1
            else:
                return -1
        if (n<0):
            return (1/self.myPow(x, -n))
        if (n==0):
            return 1
        xn2 = self.myPow(x, n//2)
        if (n%2==0):
            return (xn2*xn2)
        else:
            return (x*xn2*xn2)