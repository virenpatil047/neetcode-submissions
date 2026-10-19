class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            k = i + 1
            s = set()
            while k < len(nums):
                if -(nums[i] + nums[k]) in s:
                    l = sorted([nums[i], -(nums[i] + nums[k]), nums[k]])
                    ans.add(tuple(l))
                else:
                    s.add(nums[k])
                k += 1
        return list(ans)

            
        # nums.sort()
        # ans = []
        # for i in range(len(nums)):
        #     if i > 0 and nums[i - 1] == nums[i]:
        #         continue
        #     j = i + 1
        #     k = len(nums) - 1
        #     while(j < k):
        #         if nums[i] + nums[j] + nums[k] < 0:
        #             j += 1
        #             while j < k and nums[j - 1] == nums[j]: j+=1
        #         elif nums[i] + nums[j] + nums[k] > 0:
        #             k -= 1
        #             while j < k and nums[k + 1] == nums[k]: k-=1
        #         else:
        #             ans.append([nums[i], nums[j], nums[k]])
        #             j += 1
        #             k -= 1
        #             while j < k and nums[j - 1] == nums[j]: j+=1
        #             while j < k and nums[k + 1] == nums[k]: k-=1
        # return ans
            