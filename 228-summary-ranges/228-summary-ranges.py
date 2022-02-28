class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret = []
        if (len(nums)==0):
            return ret
        if (len(nums)==1):
            return [str(nums[0])]
        app = [None, '->', None]
        prev = None
        for no in nums:
            if (prev==None):
                app[0] = str(no)
                prev = no
                continue
            if (no==(prev+1)):
                app[2] = str(no)
            else:
                if (app[2]==None):
                    ret.append(app[0])
                else:
                    ret.append(''.join(app))
                    app[2] = None
                app[0] = str(no)
            prev = no
        #no = nums.pop()
        if (app[2]!=None):
            ret.append(''.join(app))
        else:
            ret.append(app[0])
        return ret