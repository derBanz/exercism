"""
Set task: Detect saddle points in matrix (list).
Method:
* Going through each value in matrix we compare them with the values in their row/column.
* If it fulfills the requirements the data is appended to saddles (list).
Example: saddle_points([[4, 5, 4], [3, 5, 5], [1, 5, 4]])
-> [{'row': 1, 'column': 2}, {'row': 2, 'column': 2}, {'row': 3, 'column': 2}]
"""


def saddle_points(matrix):
    saddles = list()
    try:
        rows = len(matrix)
        columns = len(matrix[0])
    except IndexError:
        return saddles
    for r in range(rows):
        if len(matrix[r]) != columns:
            raise ValueError("Matrix has to be regular.")
        for c in range(columns):
            if matrix[r][c] == max(matrix[r]) and matrix[r][c] == min([x[c] for x in matrix]):
                saddles.append({"row": r + 1, "column": c + 1})
    return saddles
    