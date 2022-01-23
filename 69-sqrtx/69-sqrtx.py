class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x<2):
            return x
        n = x//2
        #for i in range(1, n+1):
        i = 1
        while(i<n+1):
            if (i*i == x):
                return i
            if (i*i > x):
                return (i-1)
            i+=1
        return n