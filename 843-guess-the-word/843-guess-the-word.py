# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        
        guess = 0
        letGuessed = 0
        numguesses = 10
        
        def numMatch(w1, w2):
            cnt = 0
            for i in range(6):
                if w1[i]==w2[i]:
                    cnt += 1
            return cnt
        
        while guess<numguesses and letGuessed!=6:
            rando = random.choice(wordlist)
            letGuessed = master.guess(rando)
            sameNum = []
            for word in wordlist:
                if numMatch(rando, word)==letGuessed:
                    sameNum.append(word)
            wordlist = sameNum
            guess += 1