class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if xCenter <= x1:
            xClose = x1
        elif xCenter >= x2:
            xClose = x2
        else:
            xClose = xCenter
        
        if yCenter <= y1:
            yClose = y1
        elif yCenter >= y2:
            yClose = y2
        else:
            yClose = yCenter
        
        distance = sqrt((xClose - xCenter)**2 + (yClose - yCenter)**2)

        return True if distance <= radius else False
