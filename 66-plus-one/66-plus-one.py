class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = len(digits)
        for i in reversed(range(d)):
            if digits[i]<9:
                digits[i]+=1
                break
            digits[i]=0
        if digits[0]==0:
            digits.insert(0, 1)
        return digits
            