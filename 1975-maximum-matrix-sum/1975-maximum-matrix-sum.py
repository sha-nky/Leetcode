class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        minimum = float("inf")
        negs = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    negs += 1
                total += abs(matrix[i][j])
                minimum = min(minimum, abs(matrix[i][j]))
        
        return total if negs%2==0 else (total-2*minimum)
