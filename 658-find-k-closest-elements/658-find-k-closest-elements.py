class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x<=arr[0]:
            return arr[:k]
        if x>=arr[-1]:
            return arr[-k:]
        mid = -1
        n = len(arr)
        l, r = 0, n-1
        while(l<=r):
            mid = (l+r)//2
            if arr[mid]==x or (arr[mid]<x and x<arr[mid+1]):
                break
            elif arr[mid]<x:
                l = mid+1
            else:
                r = mid-1
        hashmap = {}
        sides = [arr[i] for i in range(max(0,mid-k+1), min(n,mid+k+1))]
        for num in sides:
            hashmap[num] = abs(num-x)
        closest = [num for num,_ in sorted(hashmap.items(), key=lambda x: x[1])]
        ret = []
        ind = 0
        while(len(ret)<k):
            curr = len(ret)
            val = closest[ind]
            cnt = min(sides.count(val),k-len(ret))
            ext = [val]*cnt
            ret.extend(ext)
            ind += 1
        ret.sort()
        return ret