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