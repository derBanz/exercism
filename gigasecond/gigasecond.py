"""
Set task: Given moment (int), determine the moment that would be after a gigasecond has passed.
Method: using the timedelta function from datetime, we add moment and the timedelta of 1e9 seconds.
Example: add(datetime(2011, 4, 25, 0, 0)) -> datetime(2043, 1, 1, 1, 46, 40)
"""

from datetime import timedelta

def add(moment):
    delta=timedelta(seconds=1e9)
    return moment+delta