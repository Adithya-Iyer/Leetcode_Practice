class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        exist = set()
        ret = set()
        n = len(s)
        for i in range(n-9):
            subs = s[i:i+10]
            if subs in exist:
                ret.add(subs)
            exist.add(subs)
        return list(ret)