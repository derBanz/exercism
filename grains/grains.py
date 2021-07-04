"""
Set task: Calculate the amount of grains on the number (int) field of the chessboard as well as the total grains, assuming the amount of grains doubles with each field.
Method: For the number field, just calculate 2 to the power of number minus one. For the total, calculate 2 to the power of 64 and substract one.
Example: square(7) -> 64, total() -> 18446744073709551615
"""

def square(number):
    if number < 65 and number > 0:
        return 2**(number-1)
    raise ValueError("Invalid square.")


def total():
    return 2**64-1