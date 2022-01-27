class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        le = len(nums)
        maxor = 0
        if(le<10):
            for i in range(le-1):
                for j in range(i+1, le):
                    xor = nums[i]^nums[j]
                    if (maxor<xor):
                        maxor = xor
            return maxor
        nums.sort()
        maxp2 = 2**math.ceil(math.log2(nums[le-1]))
        def binS(target, left, right):
            if (left<=right):
                mid = left + (right-left)//2
                if (target==nums[mid]):
                    return (mid, mid)
                elif (target<nums[mid]):
                    return binS(target, left, mid-1)
                else:
                    return binS(target, mid+1, right)
            else:
                return (right, left)
        l2 = maxp2/2
        for i, nn in enumerate(nums):
            tx = maxp2 + (~nn)
            l2 = le//2
            i1=i2=0
            if(i<l2):
                i1, i2 = binS(tx, i+1, le-1)
            else:
                i1, i2 = binS(tx, 0, i-1)
            if(i1==i2):
                maxor = max(maxor, nums[i1]^nn)
            else:
                if(i1>=0):
                    maxor = max(maxor, nums[i1]^nn)
                if(i2<le):
                    maxor = max(maxor, nums[i2]^nn)
        return maxor