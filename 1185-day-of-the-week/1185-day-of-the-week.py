class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def isLeap(year):
            return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
        
        def getDays(d, m, y):
            days = d + (isLeap(y) and m > 2)
            days += sum(365 + isLeap(yr) for yr in range(1971, y))
            days += sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:m-1])

            return days
        
        weekday = getDays(day, month, year) % 7
        week = {
            0 : "Thursday",
            1 : "Friday",
            2 : "Saturday",
            3 : "Sunday",
            4 : "Monday",
            5 : "Tuesday",
            6 : "Wednesday"
        }
        
        return week[weekday]
