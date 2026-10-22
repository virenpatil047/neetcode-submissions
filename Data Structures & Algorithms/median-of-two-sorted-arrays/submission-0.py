class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        nums = []
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        while i < n1:
            nums.append(nums1[i])
            i += 1
        while j < n2:
            nums.append(nums2[j])
            j += 1
        if nums == []:
            return -1
        elif (n1 + n2) % 2 == 0:
            return (nums[(n1 + n2) // 2] + nums[((n1 + n2) // 2) - 1]) / 2
        else:
            return nums[(n1 + n2) // 2]

                
