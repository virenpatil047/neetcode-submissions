class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        max_length = 0
        for n in setNums:
            if (n - 1) not in setNums:
                length = 1
                while (n + length) in setNums:
                    length += 1
                max_length = max(max_length, length)
        return max_length