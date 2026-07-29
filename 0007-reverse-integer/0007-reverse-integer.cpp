class Solution {
public:
    int reverse(int x) {
        int rev =0;
        while(x!=0){
            int i = x%10;

        //checking for interger overflow-    
        if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && i > 7))
            return 0;
        if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && i < -8))
            return 0;

            rev =rev*10+i;
            x/=10;
        }
        return rev;
    }
};