class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        if matrix[mid][0] > target:
            mid -= 1
        low, high = 0, len(matrix[mid]) - 1
        row = mid
        mid = 0
        while low <= high:
            mid = (low + high) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        # def binary_search(arr):
        #     low, high = 0, len(arr) - 1
        #     while low <= high:
        #         mid = (low + high) // 2
        #         if arr[mid] == target:
        #             return mid
        #         elif arr[mid] < target:
        #             low = mid + 1
        #         else:
        #             high = mid - 1
        #     return mid
        # col = [m[0] for m in matrix]
        # row_index = binary_search(col)
        # if matrix[row_index][0] > target:
        #     row_index -= 1
        # row = matrix[row_index]
        # if matrix[row_index][0] == target:
        #     return True
        # else:
        #     return matrix[row_index][binary_search(row)] == target