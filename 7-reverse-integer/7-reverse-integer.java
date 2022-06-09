class Solution {
    public int reverse(int x) {
        //x = 1534236469;
        //System.out.println((int)9646324351);
        long r=0;
        while(x!=0) {
            r = r*10 + x%10;
            x/=10;
            //System.out.println(r);
        }
        if ((-2147483648 <= r) && (r <= 2147483647)) {
            return (int)r;
        } 
        else {
            return 0;
        }
    }
}