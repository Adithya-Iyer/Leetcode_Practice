class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        points = []
        x = y = 0
        points.append((x,y))
        #print (points)
        for p in path:
            if (p == 'N'):
                y+=1
            elif  (p == 'S'):
                y-=1
            elif  (p == 'E'):
                x+=1
            elif  (p == 'W'):
                x-=1
            posn = (x,y)
            if posn in points:
                return True
            points.append(posn)
        return False
