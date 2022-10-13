class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        n1, n2 = num1.split('+'), num2.split('+')
        r1, i1 = int(n1[0]), int(n1[1][:-1])
        r2, i2 = int(n2[0]), int(n2[1][:-1])
        real = r1*r2 - i1*i2
        imgry = r1*i2 + i1*r2
        ret = str(real)+'+'+str(imgry)+'i'
        return ret