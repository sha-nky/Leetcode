class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minuteAngle = 6.0 * minutes
        hourAngle = 30.0 * (hour % 12) + 0.5 * minutes

        diff = abs(hourAngle - minuteAngle)

        return min(diff, 360.0 - diff)
