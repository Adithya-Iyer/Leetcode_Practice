class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        c2 = int(c**0.5)
        a = 0
        while(a<=c2):
            b2 = c - a*a
            b = b2**0.5
            #print(c, a, b)
            if (b==int(b)):
                return True
            a+=1
        return False            