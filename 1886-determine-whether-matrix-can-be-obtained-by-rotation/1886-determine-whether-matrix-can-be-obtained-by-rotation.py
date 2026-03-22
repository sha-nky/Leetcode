class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        
        def rotate90(matrix):
            return [list(row) for row in zip(*matrix[::-1])]
        
        for _ in range(3):
            mat = rotate90(mat)
            if mat == target:
                return True
        
        return False
