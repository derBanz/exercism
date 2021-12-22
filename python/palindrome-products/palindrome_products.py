"""
Set task: Detect palindrome products in a given range.
Method:
Example:
"""


def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor cannot be bigger than max_factor.")
    a = b = max_factor
    pal = p = 0
    while a >= min_factor and b >= min_factor and a ** 2 >= p:
        pal = a * b
        if str(pal) == str(pal)[::-1]:
            p = pal
        if a * (b - 1) < p or b == min_factor:
            a -= 1
            b = a
        else:
            b -= 1
    if str(p) != str(p)[::-1] or p == 0:
        return None, []
    facts = list()
    for x in range(min_factor, max_factor):
        if not p % x and p / x <= max_factor and [int(p / x), x] not in facts:
            facts.append([x, int(p / x)])
    return p, facts


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor cannot be bigger than max_factor.")
    a = b = min_factor
    pal = p = max_factor ** 2 + 1
    while a <= max_factor and b <= max_factor and a ** 2 <= p:
        pal = a * b
        if str(pal) == str(pal)[::-1]:
            p = pal
        if a * (b + 1) > p or b == max_factor:
            a += 1
            b = a
        else:
            b += 1
    if str(p) != str(p)[::-1] or p == max_factor ** 2 + 1:
        return None, []
    facts = list()
    for x in range(min_factor, max_factor):
        if not p % x and p / x >= min_factor and [int(p / x), x] not in facts:
            facts.append([x, int(p / x)])
    return p, facts
