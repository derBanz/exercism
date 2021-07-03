def square(number):
    if number < 65 and number > 0:
        return 2**(number-1)
    raise ValueError("Invalid square.")


def total():
    return 2**64-1
