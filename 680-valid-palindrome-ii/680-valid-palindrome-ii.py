class Solution:
    def validPalindrome(self, s: str) -> bool:
        letters = len(s)
        if(letters<=2):
            return True
        def forward():
            delete = 0
            for ind in range(letters//2):
                if s[ind]==s[letters-(ind+delete+1)]:
                    continue
                else:
                    if delete==1:
                        return False
                    delete=1
                    if s[ind]==s[letters-(ind+delete+1)]:
                        continue
                    return False
            return True
        def backward():
            delete = 0
            for ind in range(letters//2):
                if s[ind+delete]==s[letters-(ind+1)]:
                    continue
                else:
                    if delete==1:
                        return False
                    delete=1
                    if s[ind+delete]==s[letters-(ind+1)]:
                        continue
                    return False
            return True
        return (forward() or backward())