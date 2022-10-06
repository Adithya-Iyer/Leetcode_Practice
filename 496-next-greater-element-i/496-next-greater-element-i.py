class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nrange = (min(nums2), max(nums2))
        least = min(nums2)
        hashmap = {}
        visited = set()
        for n in reversed(nums2):
            for i in range(least, n):
                if i not in visited:
                    hashmap[i] = n
            visited.add(n)
        ans = []
        for x in nums1:
            ans.append(hashmap.get(x, -1))
        return ans