class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        inc = True
        n = len(arr)
        if n<3:
            return False
        for i in range(1, n):
            if inc:
                if arr[i-1]==arr[i]:
                    return False
                elif arr[i-1]>arr[i]:
                    if i==1:
                        return False
                    inc = False
            else:
                if arr[i-1]<=arr[i]:
                    return False
        return not inc