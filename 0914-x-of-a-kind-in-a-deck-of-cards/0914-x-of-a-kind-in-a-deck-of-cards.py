class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hashmap = {}
        for n in deck:
            hashmap[n] = hashmap.get(n,0) + 1
        least = len(deck)
        for k in hashmap:
            if least>hashmap[k]:
                least=hashmap[k]
        if least==1:
            return False
        def gcd(x,y):
            if y==0:
                return abs(x)
            return gcd(y,x%y)
        for k in hashmap:
            least = gcd(hashmap[k], least)
        return (least>1)        