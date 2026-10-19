class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}
        for i in range(0, len(nums)):
            k = target - nums[i]
            if k not in mpp.keys():
                mpp[nums[i]] = i
            else:
                return [mpp[k], i]
        return [-1, -1]