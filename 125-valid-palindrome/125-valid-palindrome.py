class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []
        for char in s:
            if char.isalnum():
                letters.append(char.lower())
        le = len(letters)
        if (le<=1):
            return True
        #print(letters)
        for ind in range(le//2):
            if not (letters[ind]==letters[le-ind-1]):
                return False
        return True