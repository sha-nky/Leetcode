class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isLeap(year):
            return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
        
        def getDays(date):
            y, m, d = map(int, date.split("-"))

            days = d + int(isLeap(y) and m > 2)
            days += sum(365 + int(isLeap(year)) for year in range(1971, y))
            days += sum([0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:m])

            return days
        
        return abs(getDays(date1) - getDays(date2))
