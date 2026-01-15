class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        maxHor = 1 if not hBars else 2
        maxVer = 1 if not vBars else 2
        count = 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i-1] + 1:
                count += 1
            else:
                count = 1
            maxHor = max(maxHor, count + 1)
        
        count = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i-1] + 1:
                count += 1
            else:
                count = 1
            maxVer = max(maxVer, count + 1)
        
        side = min(maxHor, maxVer)
        return side * side
