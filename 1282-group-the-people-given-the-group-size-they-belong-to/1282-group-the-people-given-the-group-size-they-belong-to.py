class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size = {}
        for i in range(len(groupSizes)):
            sz = groupSizes[i]
            if sz in size:
                size[sz].append(i)
            else:
                size[sz] = [i]
        grps = []
        for sz in size:
            arr = size[sz]
            for i in range(len(arr)//sz):
                grps.append(arr[i*sz : (i+1)*sz])
        return grps