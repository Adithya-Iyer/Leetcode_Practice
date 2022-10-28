class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letDict = {}
        for word in strs:
            sw = ''.join(sorted(list(word)))
            if sw in letDict:
                letDict[sw].append(word)
            else:
                letDict[sw] = [word]
        return letDict.values()