class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int currMax = 0;
        int l = prices[0];
        for(int i = 0; i < prices.length; i++){
            currMax = prices[i]-l;
            if(prices[i]<l){
                l = prices[i];
            }
            if (currMax > max){
                max = currMax;
            }
        }
        return max;
    }
}
