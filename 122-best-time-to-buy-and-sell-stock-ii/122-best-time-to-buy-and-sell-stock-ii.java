class Solution {
    public int maxProfit(int[] prices) {
        int days = prices.length;
        if (days<=1)
            return 0;
        boolean hold = (prices[0]<=prices[1])?true:false;
        int cp=Integer.MAX_VALUE, sp=0, i=1, maxProfit=0;
        if (hold)
            cp = prices[0];
        for(;i<days-1;i++) {
            if ((prices[i]<=prices[i-1])&&(prices[i]<prices[i+1])) {
                cp = prices[i];
                hold = true;
                System.out.println("Buy on "+i+" day at "+cp);
            }
            else if ((prices[i]>prices[i-1])&&(prices[i]>=prices[i+1])) {
                sp = prices[i];
                maxProfit+=sp-cp;
                hold = false;
                System.out.println("Sell on "+i+" day at "+sp);
            }
        }
        if (prices[i]>prices[i-1])
            maxProfit+=prices[i]-cp;
        return maxProfit;
    }
}