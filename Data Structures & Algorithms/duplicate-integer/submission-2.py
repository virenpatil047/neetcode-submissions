class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mpp = {}
        for n in nums:
            if n not in mpp.keys():
                mpp[n] = 1
            else:
                return True
        return False