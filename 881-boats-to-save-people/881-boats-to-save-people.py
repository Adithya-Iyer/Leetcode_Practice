class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        p = len(people)
        boats = 0
        i, j = 0, p-1
        while (i<=j):
            boats +=1
            if i==j:
                break
            if people[i]+people[j] <= limit:
                i, j = i+1, j-1
            else:
                j -= 1
        return boats