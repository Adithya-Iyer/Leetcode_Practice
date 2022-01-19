class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag = list(magazine)
        for letter in ransomNote:
            if letter not in mag:
                return False
            mag.remove(letter)
        return True