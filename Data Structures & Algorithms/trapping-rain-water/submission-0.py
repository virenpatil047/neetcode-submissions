class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax, amount = 0, 0, 0
        while l < r :
            if height[l] <= height[r]:
                if height[l] > lmax:
                    lmax = height[l]
                else:
                    amount += lmax - height[l]
                l += 1
            else:
                if height[r] > rmax:
                    rmax = height[r]
                else:
                    amount += rmax - height[r]
                r -= 1
        return amount
        