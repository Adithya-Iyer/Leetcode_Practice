import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend==0):
            return 0
        isNeg = (dividend<0)^(divisor<0)
        nume = abs(dividend)
        deno = abs(divisor)
        quo = 0
        if (deno>nume):
            quo = 0
        elif (deno==1):
            quo = nume
        elif (math.log2(deno)==int(math.log2(deno))):
            quo = nume >> int(math.log2(deno))
        else:
            i = 31
            while (nume>0 and i>=0):
                if (nume<deno):
                    break
                x = deno << i
                if (x<=nume):
                    nume -= x
                    quo += 1 << i
                i-=1
        if (isNeg):
            if (quo>2147483648):
                return -2147483648
            else:
                return -(quo)
        else:
            if (quo>2147483647):
                return 2147483647
            else:
                return quo