class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sfin = []
        for schar in s:
            if schar=='#':
                if sfin:
                    sfin.pop()
            else:
                sfin.append(schar)
        tfin = []
        for tchar in t:
            if tchar=='#':
                if tfin:
                    tfin.pop()
            else:
                tfin.append(tchar)
        if tfin==sfin:
            return True
        else:
            return False