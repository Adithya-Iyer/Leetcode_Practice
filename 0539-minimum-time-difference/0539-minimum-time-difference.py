class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minsPts = []
        for time in timePoints:
            hrs = int(time[:2])
            mins = int(time[3:])
            t = hrs*60 + mins
            minsPts.append(t)
        minsPts.sort()
        minsPts.append(minsPts[0]+1440)
        ret = 720
        n = len(minsPts)
        for i in range(n-1):
            diff = minsPts[i+1]-minsPts[i]
            if diff==0:
                return 0
            ret = min(ret, diff)
        return ret