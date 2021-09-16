"""
Set Task: Convert number (int) into a string that contains raindrop sounds corresponding to number's factors.
Method:
* The modulo of number is compared to the prerequisite numbers. On a match, a String gets added to result (String).
Example: convert(120) -> "PlingPlang"
"""

def convert(number):
    result = ""
    if number % 3 == 0: result = result + "Pling"
    if number % 5 == 0: result = result + "Plang"
    if number % 7 == 0: result = result + "Plong"
    if len(result) == 0: result = result + str(number)
    return result