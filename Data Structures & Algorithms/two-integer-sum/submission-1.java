class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> diff = new HashMap<>();
        for(int i = 0; i <= nums.length; i++){
            int difference = target - nums[i];
            if(diff.containsKey(difference)){
                return (i>diff.get(difference)) ? new int[] {diff.get(difference),i} : new int[] {i, diff.get(difference)};
            }
            diff.put(nums[i], i);
        }
        return null;
    }
}
