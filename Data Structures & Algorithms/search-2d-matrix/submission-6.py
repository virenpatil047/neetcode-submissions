class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, (m * n) - 1
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if matrix[mid // n][mid % n] > target:
                high = mid - 1
            elif matrix[mid // n][mid % n] < target:
                low = mid + 1
            else:
                return True
        return False