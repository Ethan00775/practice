class Solution {
    public boolean hasDuplicate(int[] nums) {
        ArrayList<Integer> used = new ArrayList<>();
        for(int x:nums){
            if(used.contains(x)){
                return true;
            }
            used.add(x);
        }
        return false;
    }
}