class Solution {
    public int largestAltitude(int[] gain) {
        int n = gain.length;
        // int alt[] = new int[n+1];
        // alt[0]=0;
        int ans = 0;
        int sum = 0;
        for (int i = 0; i<n;i++){
            // alt[i+1]=alt[i]+nums[i];
            sum +=gain[i];
            if(sum>ans){
                ans=sum;
            }
        }
        return ans;
        // int max = alt[0];
        // for (int i = 1; i < alt.length; i++) {
        //     if (alt[i] > max) {
        //         max = alt[i]; 
        //     }      
        // }

    }
}