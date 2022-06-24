class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sl = len(strs)
        if strs==1:
            return strs[0]
        prefix = []
        ref = strs[0]
        nomatch = False
        for i in range(len(ref)):
            for word in strs:
                if i>=len(word) or word[i]!=ref[i]:
                    nomatch = True
                    break
            if nomatch:
                break
            prefix.append(ref[i])
        return ''.join(prefix)