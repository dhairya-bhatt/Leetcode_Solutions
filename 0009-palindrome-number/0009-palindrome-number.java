class Solution {
    public boolean isPalindrome(int x) {
        if (x <0){
            return false;
        }else{
            String str = Integer.toString(x);
            String reversedStr = new StringBuilder(str).reverse().toString();
            long reversedObject = Long.parseLong(reversedStr);
            return reversedObject == x;
        }
    }
}