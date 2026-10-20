class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr):
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return mid
        col = [m[0] for m in matrix]
        row_index = binary_search(col)
        if matrix[row_index][0] > target:
            row_index -= 1
        row = matrix[row_index]
        if matrix[row_index][0] == target:
            return True
        else:
            return matrix[row_index][binary_search(row)] == target