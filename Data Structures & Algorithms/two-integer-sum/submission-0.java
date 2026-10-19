class Solution {
    public int[] twoSum(int[] nums, int k) {
        HashMap<Integer, Integer> mpp = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(mpp.containsKey(k-nums[i]))return new int[]{mpp.get(k-nums[i]),i};
            else mpp.put(nums[i],i);
        }
        return new int[]{0,1};
    }
}
