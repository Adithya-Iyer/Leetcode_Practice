class Solution:
    def frequencySort(self, s: str) -> str:
        charDict = {}
        for ch in s:
            charDict[ch] = charDict.get(ch, 0) + 1
        charDict = {k:v for k, v in sorted(charDict.items(), key=lambda item: item[1], reverse=True)}
        answer = []
        for key in charDict:
            for i in range(charDict[key]):
                answer.append(key)
        return ''.join(answer)