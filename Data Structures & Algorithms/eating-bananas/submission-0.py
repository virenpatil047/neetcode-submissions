class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            time = 0
            for p in piles: time += math.ceil(p / mid)
            if time <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low