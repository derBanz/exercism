"""
Set task: Add the mine counts to a completed Minesweeper board.
Method: Going through each character, check if it's a mine or a space. If it's
        a space, count the mines around it and add it.
Example: annotate([" * * "]) -> ["1*2*1"]
"""


def annotate(minefield):
    res = list()
    try:
        height = len(minefield)
        width = len(minefield[0])
    except IndexError:
        return res
    for row in range(height):
        res.append("")
        if len(minefield[row]) != width:
            raise ValueError("Inconsistent field.")
        for char in range(len(minefield[row])):
            if minefield[row][char] == "*":
                res[-1] += "*"
            elif minefield[row][char] == " ":
                mines = 0
                min_x = min_y = -1
                max_x = max_y = 2
                if row == 0:
                    min_x = 0
                if row == height - 1:
                    max_x = 1
                if char == 0:
                    min_y = 0
                if char == len(minefield[row]) - 1:
                    max_y = 1
                for x in range(min_x, max_x):
                    for y in range(min_y, max_y):
                        if x == 0 and y == 0:
                            continue
                        mines += minefield[row + x][char + y] == "*"
                if mines == 0:
                    res[-1] += " "
                else:
                    res[-1] += str(mines)
            else:
                raise ValueError("Invalid character on board.")
    return res


print(annotate([" * * "]))
