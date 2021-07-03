def is_armstrong_number(number):
    check=0
    number=str(number)
    for s in range(len(number)):
        check+=pow(int(number[int(s)]),len(number))
    return check==int(number)