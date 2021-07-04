"""
Set task: Check, whether a given year (int) is a leap year or not. A leap year occurse on every year that is divisible by 4 except for years that are divisible by 100 unless the year is divisible by 400.
Method: We check whether the year is divisible by 400 or whether it is divisible by 4 and not divisible by 100.
Example: leap_year(1992) -> True
"""

def leap_year(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return True
    return False