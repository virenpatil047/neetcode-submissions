class Solution {
public:
    bool hasDuplicate(vector<int>& n) {
        map<int,int> mpp;
        for(auto i : n){
            mpp[i]++;
            if(mpp[i]>1)return true;
        }
        return false;
    }
};