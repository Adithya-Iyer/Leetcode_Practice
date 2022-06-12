class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = list(str(num))
        for d in range(len(digits)):
            if digits[d]=='6':
                digits[d]='9'
                return int(''.join(digits))
        return num