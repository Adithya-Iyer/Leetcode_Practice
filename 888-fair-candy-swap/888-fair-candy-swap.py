class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aSum = sum(aliceSizes)
        bSum = sum(bobSizes)
        asL = sorted(list(set(aliceSizes)))
        bsL = sorted(list(set(bobSizes)))
        # asL = sorted(aliceSizes)
        # bsL = sorted(bobSizes)
        an, bn = len(asL), len(bsL)
        ap = bp = 0
        while(ap<an and bp<bn):
            d = asL[ap]-bsL[bp]
            at, bt = aSum-d, bSum+d
            if (at==bt):
                break
            elif (at>bt):
                ap+=1
            elif (at<bt):
                bp+=1
        return [asL[ap],bsL[bp]]