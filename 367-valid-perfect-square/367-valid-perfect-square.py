class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        #for i in range(1, n+1):
        i = 1
        while(i<num+1):
            if (i*i == num):
                return True
            if (i*i > num):
                return False
            i+=1
        return False