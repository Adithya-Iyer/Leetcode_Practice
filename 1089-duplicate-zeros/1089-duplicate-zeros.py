class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        nonzero = []
        for a in arr:
            nonzero.append(a)
        n = len(arr)
        i = j = 0
        while(i<n and j<n):
            arr[j] = nonzero[i]
            if nonzero[i]==0:
                j += 1
                if j<n:
                    arr[j] = 0
            i, j = i+1, j+1
        