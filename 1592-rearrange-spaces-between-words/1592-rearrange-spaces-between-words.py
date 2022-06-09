class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        numSpaces = text.count(' ')
        numWords = len(words)
        reordered = []
        endSpace = numSpaces
        if numWords>1:
            midSpace = numSpaces//(numWords-1)
            spaces = []
            for j in range(midSpace):
                spaces.append(' ')
            spaceText = ''.join(spaces)
            endSpace = numSpaces%(numWords-1)
            for i in range(numWords-1):
                reordered.append(words[i])
                reordered.append(spaceText)
        reordered.append(words.pop())
        end = []
        for j in range(endSpace):
            end.append(' ')
        endText = ''.join(end)
        reordered.append(endText)
        return ''.join(reordered)