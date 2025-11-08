class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        low, high = 0, (len(matrix) * n)-1

        while low <= high:
            mid = low + (high-low)//2
            row, col = divmod(mid, n)
            mid_val = matrix[row][col]

            if mid_val == target: return True
            elif mid_val > target: high = mid-1
            else: low = mid+1

        return False