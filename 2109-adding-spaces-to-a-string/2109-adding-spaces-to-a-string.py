class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        li = ri = 0
        final = []
        for ss in spaces:
            ri = ss
            final.append(s[li:ri])
            li = ri
        final.append(s[li:])
        return ' '.join(final)