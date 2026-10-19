class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n = sorted(set(nums))
        print(n)
        max_cnt, cnt = 1, 1
        for i in range(len(n) - 1):
            if n[i + 1] - n[i] == 1:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt) 
                cnt = 1
        return max(max_cnt, cnt)