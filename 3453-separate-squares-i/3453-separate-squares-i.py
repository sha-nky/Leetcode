class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        if not squares:
            return 0
        
        totalArea = sum(l*l for _, _, l in squares)
        halfArea = totalArea / 2

        low = min(y for _, y, _ in squares)
        high = max(y+l for _, y, l in squares)

        def belowArea(Y):
            total = 0
            for _, y, l in squares:
                if Y <= y:
                    continue
                total += min(Y-y, l) * l
            return total
        
        for _ in range(60):
            mid = (low + high) / 2
            if belowArea(mid) < halfArea:
                low = mid
            else:
                high = mid
        
        return (low + high) / 2
