class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)

        if start > end:
            return 0
        
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        startDay = sum(days[:int(start[:2]) - 1]) + int(start[3:])
        endDay = sum(days[:int(end[:2]) - 1]) + int(end[3:])
        
        return endDay - startDay + 1
