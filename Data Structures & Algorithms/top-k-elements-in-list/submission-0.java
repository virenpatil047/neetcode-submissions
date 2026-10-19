class Solution {
    int[] max_map(HashMap<Integer,Integer> mpp) {
            Map.Entry<Integer, Integer> first = mpp.entrySet().iterator().next();
            int key = -1;
            int value = Integer.MIN_VALUE;
            for (Map.Entry<Integer,Integer> m : mpp.entrySet()) {
                if(m.getValue()>value){
                    key = m.getKey();
                    value = m.getValue();
                }
            }
            return new int[]{key,value};
        }
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> mpp = new HashMap<>();
        for(int i : nums){
            if(mpp.containsKey(i)){
                mpp.put(i,mpp.get(i)+1);
            }
            else mpp.put(i,1);
        }
        int[] arr = new int[k];
        for(int i=0;i<k;i++){
            int[] val = new int[2];
            val = max_map(mpp);
            mpp.remove(val[0]);
            arr[i]=val[0];
        }
        return arr;
    }
}
