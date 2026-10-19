class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> mpp = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            if(mpp.containsValue(nums[i]))return true;
            mpp.put(i,nums[i]);
        }
        return false;

    }
}