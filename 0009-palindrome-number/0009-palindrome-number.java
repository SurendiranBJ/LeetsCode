class Solution {
    public boolean isPalindrome(int x) {
        if (x<0){
            return false;
        }
        String let=Integer.toString(x);
        String rev=new StringBuilder(let).reverse().toString();
        if(let.equals(rev)){
            return true;
        }
        else{
            return false;
        }
    }
}