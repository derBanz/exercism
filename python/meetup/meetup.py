"""
Set task: Given a general description, provide the exact date of a planned meetup. Given are year (int), month (int), week (String) and day_of_week (String).
Method: 
* We go through each day of a week and compare the date with the day_of_week.
* If week is given as "1st" to "5th", the check starts at the (7*week + 1) of the month and ends 7 days later, going through all weekdays.
* If week is given as "last", the check starts at the 31st of the month and ends 10 days earlier, going through all weekdays.
* If week is given as "teenth" the check starts at the 13th of the month and ends at the 19th, going through all weekdays.
Example: meetup(2013, 6, "2nd", "Tuesday") -> date(2013, 6, 11)
"""

from datetime import date

class MeetupDayException(Exception):
    pass

def meetup(year, month, week, day_of_week):
    days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weeks=["1st", "2nd", "3rd", "4th", "5th", "last", "teenth"]
    week=weeks.index(week)
    if week < 5:
        for i in range(7):
            try:
                res=date(year, month, (7 * week) + i + 1)
                if res.weekday() == days.index(day_of_week):
                    return res
            except:
                pass
    elif week == 5:
        for i in range(10):
            try:
                res=date(year, month, 31 - i)
                if res.weekday() == days.index(day_of_week):
                    return res
            except:
                pass
    elif week == 6:
        for i in range(13,20):
            res=date(year, month, i)
            if res.weekday() == days.index(day_of_week):
                return res
    
    raise MeetupDayException("This does not work!")