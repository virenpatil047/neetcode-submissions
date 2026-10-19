class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for n in nums:
            seen[n] = 1 + seen.get(n, 0)
        buckets = [[] for n in range(len(nums) + 1)]
        for val, cnt in seen.items():
            buckets[cnt].append(val)
        cnt = 0
        ans = []
        for i in range(len(nums), -1, -1):
            for n in buckets[i]:
                ans.append(n)
                cnt += 1
                if cnt == k:
                    return ans
