class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        past = set()
        for ele in arr:
            if (((2*ele) in past) or ((0.5*ele)==(ele//2) and ((ele//2) in past))):
                return True
            past.add(ele)
        return False