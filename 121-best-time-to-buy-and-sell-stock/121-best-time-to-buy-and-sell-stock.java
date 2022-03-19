class Solution {
    public int maxProfit(int[] prices) {
        int buy=-1, sell=-1, maxProfit=0, leastPrice=0;
        for (int i=1; i<prices.length; i++) {
            if (prices[i]<prices[leastPrice])
                leastPrice=i;
            else {
                int profit = prices[i] - prices[leastPrice];
                if (profit>maxProfit) {
                    maxProfit = profit;
                    sell = i;
                    buy = leastPrice;
                }
            }
        }
        if (buy==-1)
            System.out.println("No transaction");
        else
            System.out.println("Buy on day "+(buy+1)+" at "+(prices[buy])+" and sell on day "+(sell+1)+" at "+(prices[sell]));
        return maxProfit;
    }
}