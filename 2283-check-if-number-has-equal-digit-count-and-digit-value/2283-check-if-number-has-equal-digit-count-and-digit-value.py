class Solution:
    def digitCount(self, num: str) -> bool:
        n = len(num)
        hashmap = {str(i): 0 for i in range(n)}
        for d in num:
            if d not in hashmap:
                return False
            hashmap[d] += 1
        for i in range(n):
            if int(num[i])!=hashmap[str(i)]:
                return False
        return True