class Solution {
    public boolean isPalindrome(String s) {
        String result = s.replaceAll("[^a-zA-Z0-9]", "");
        for(int i = 0; i < (result.length()/2); i++){
            if(!(result.substring(i,i+1).toLowerCase().equals(result.substring(result.length()-i-1,result.length()-i).toLowerCase()))){
                return false;
            }
        }
        return true;
    }
}
