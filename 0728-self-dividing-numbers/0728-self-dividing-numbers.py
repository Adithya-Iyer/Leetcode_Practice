class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []
        for num in range(left, right+1):
            cp = num
            slfd = True
            while(cp>0):
                d = cp%10
                cp //= 10
                if d==0 or num%d!=0:
                    slfd = False
                    break
            if slfd:
                ret.append(num)
        return ret