class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words = sorted(words, key = lambda x: len(x))
        licenseWords = [ch.lower() for ch in licensePlate if ch.isalpha()]
        for wrd in words:
            clist = list(wrd)
            complete = True
            for letter in licenseWords:
                if letter not in clist:
                    complete = False
                    break
                clist.remove(letter)
            if complete:
                return wrd
        return ''