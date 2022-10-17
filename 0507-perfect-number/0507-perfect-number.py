class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<6:
            return False
        divisors = [1]
        i, j = 2, num
        while(i<j and (i*i <= num)):
            if num%i==0:
                j = num//i
                divisors.extend([i,j])
            i += 1
        if sum(divisors)==num:
            return True
        return False