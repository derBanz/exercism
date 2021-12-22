"""
Set task: Given a 3 x 4 grid of pipes, underscores, and spaces, determine which
          number is represented, or whether it is garbled.
Method:
* We first check, whether the basic format is correct (lines is multiple of 4,
  columns is multiple of 3) and throw an error in case this is incorrect.
* We then loop through input_grid and split the individual numbers up. The
  outer list of individuals contains all numbers. The next level denotes the
  rows of numbers. The bottom level is the individual numbers.
* Once we split up the individual numbers we loop through individuals and
  compare each entry against a prepared database of all numbers.
Example:
convert([
    "       _ ",
    "  |  || |",
    "  |  ||_|",
    "         ",
])
(->
[[[
    '   ',
    '  |',
    '  |',
    '   '
], [
    '   ',
    '  |',
    '  |',
    '   '
], [
    ' _ ',
    '| |',
    '|_|',
    '   '
]]]
) -> "110"
"""


def convert(input_grid):
    res = ""
    if len(input_grid) % 4 or len(input_grid[0]) % 3:
        raise ValueError("Incorrect input format.")
    individuals = list()
    for i in range(len(input_grid)):
        if not i % 4:
            individuals.append([])
        for j in range(len(input_grid[i])):
            if not j % 3 and not i % 4:
                individuals[int(i / 4)].append([])
            if not j % 3:
                individuals[int(i / 4)][int(j / 3)].append(input_grid[i][j])
            else:
                individuals[int(i / 4)][int(j / 3)][i % 4] += input_grid[i][j]
    database = [
        [" _ ", "| |", "|_|", "   "],
        ["   ", "  |", "  |", "   "],
        [" _ ", " _|", "|_ ", "   "],
        [" _ ", " _|", " _|", "   "],
        ["   ", "|_|", "  |", "   "],
        [" _ ", "|_ ", " _|", "   "],
        [" _ ", "|_ ", "|_|", "   "],
        [" _ ", "  |", "  |", "   "],
        [" _ ", "|_|", "|_|", "   "],
        [" _ ", "|_|", " _|", "   "],
    ]
    print(individuals)
    for block in individuals:
        for char in block:
            try:
                res += str(database.index(char))
            except ValueError:
                res += "?"
        res += ","
    return res[:-1]
