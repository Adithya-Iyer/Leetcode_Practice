class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n==1:
            return ""
        word = list(palindrome)
        broken = False
        for i in range(n//2):
            if word[i] != 'a':
                word[i] = 'a'
                broken = True
                break
        if not broken:
            word[-1] = 'b'
        return ''.join(word)