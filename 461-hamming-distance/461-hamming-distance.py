class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        for i in range(33):
            p2 = 2**i
            if (p2&x != p2&y):
                count+=1
        return count