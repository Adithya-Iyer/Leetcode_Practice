class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return False
        letters = set()
        for ch in sentence:
            letters.add(ch)
            if len(letters)==26:
                return True
        return False