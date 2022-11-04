class Solution:
    def reverseVowels(self, s: str) -> str:
        ch = list(s)
        v = {'a','e','i','o','u','A','E','I','O','U'}
        l = len(s)
        i, j = 0, l-1
        while(i<j):
            if ch[i] not in v:
                i += 1
            if ch[j] not in v:
                j -= 1
            if ch[i] in v and ch[j] in v:
                ch[i], ch[j] = ch[j], ch[i]
                i, j = i+1, j-1
        return ''.join(ch)