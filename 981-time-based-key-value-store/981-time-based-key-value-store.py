class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        vt = self.hashmap.get(key, [])
        vt.append([value,timestamp])
        n = len(vt)
        for i in reversed(range(1,n)):
            if vt[i][1]>vt[i-1][1]:
                break
            vt[i][1], vt[i-1][1] = vt[i-1][1], vt[i][1]
        self.hashmap[key] = vt

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        vt = self.hashmap[key]
        n = len(vt)
        l, r = 0, n-1
        if vt[l][1]>timestamp:
            return ""
        while(l<=r):
            mid = (l+r)//2
            if vt[mid][1]==timestamp:
                return vt[mid][0]
            if vt[l][1]>timestamp:
                return vt[l-1][0]
            if vt[r][1]<timestamp:
                return vt[r][0]
            if vt[mid][1]>timestamp:
                r = mid-1
            if vt[mid][1]<timestamp:
                l = mid+1
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)