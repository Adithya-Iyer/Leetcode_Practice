class Solution {
    
    public int hammingDistance(int x, int y) {
        /*int count = 0;
        for (int i=0; i<31; i++) {
            int p2 = 1<<i;
            if ((p2&x)!=(p2&y))
                count++;
        }
        return count;*/
        return Integer.bitCount(x^y);
    }
    
    public int totalHammingDistance(int[] nums) {
        int n = nums.length;
        int hd = 0;
        for (int i=0; i<n-1; i++) {
            for (int j=i+1; j<n; j++)
                hd+=hammingDistance(nums[i], nums[j]);
        }
        return hd;
    }
    
    
    
}