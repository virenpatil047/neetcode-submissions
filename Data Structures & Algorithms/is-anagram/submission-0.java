class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!= t.length())return false;
        int[] arr = new int[26];
        for (char i : s.toCharArray()) {
            arr[i-'a']++;
        }
        for (char i : t.toCharArray()) {
            arr[i-'a']--;
        }
        for(var i : arr){
            if(i!=0)return false;
        }
        return true;
    }
}
