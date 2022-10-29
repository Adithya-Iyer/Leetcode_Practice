class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        zipped_lists = zip(growTime, plantTime)
        sorted_pairs = sorted(zipped_lists, reverse=True)
        tuples = zip(*sorted_pairs)
        growTime, plantTime = [ list(tup) for tup in  tuples]
        plantDay = [plantTime[0]]
        bloomDay = [(plantTime[0]+growTime[0])]
        for i in range(1, len(plantTime)):
            plantDay.append((plantDay[i-1]+plantTime[i]))
            bloomDay.append((plantDay[i]+growTime[i]))
        return (max(bloomDay))