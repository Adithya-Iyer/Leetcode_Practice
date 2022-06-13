class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or len(word)==1 or word[1:].islower():
            return True
        return False