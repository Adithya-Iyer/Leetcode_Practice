class Solution:
    def numberOfWays(self, corridor: str) -> int:
        """seatCounter = [0]
        plantCounter = []
        s = x = y = 0
        n = len(corridor)
        for i, c in enumerate(corridor):
            if (c=='S'):
                if (seatCounter[s]==2):
                    seatCounter.append(0)
                    s+=1
                    y = i
                    plantCounter.append(y-x)
                seatCounter[s]+=1
                if (seatCounter[s]==2):
                    x = i
        if(seatCounter[s]<2):
            return 0
        return (math.prod(plantCounter)%(10**9 + 7))"""
        plantCounter = []
        seat = x = y = 0
        n = len(corridor)
        for i, c in enumerate(corridor):
            if (c=='S'):
                if (seat==2):
                    seat = 0
                    y = i
                    plantCounter.append(y-x)
                seat+=1
                if (seat==2):
                    x = i
        if(seat<2):
            return 0
        return (math.prod(plantCounter)%(10**9 + 7))