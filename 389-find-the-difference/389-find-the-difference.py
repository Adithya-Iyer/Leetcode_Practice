class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = {}
        for tchar in t:
            if tchar in letters:
                letters[tchar]+=1
            else:
                letters[tchar]=1
        for schar in s:
            letters[schar]-=1
        for key in letters:
            if letters[key]>0:
                return key
        return ''