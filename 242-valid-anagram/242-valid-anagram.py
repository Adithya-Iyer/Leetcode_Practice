class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls = list(s)
        lt = list(t)
        if not (len(ls)==len(lt)):
            return False
        for c in ls:
            if c not in lt:
                return False
            lt.remove(c)
        return True