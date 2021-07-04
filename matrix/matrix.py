"""
Set task: For a given matrix_string (String), provide a specific row or column.
Method:
* matrix_string is split along the newlines and saves as self.rows (list). The strings in self.rows further get split along the space, so the rows contain listed integers.
* We loop through self.rows and initiate self.columns (list) to have the proper amount of entries according to the amount of columns. 
* We loop again through self.rows and self.columns to populate self.columns.
* row() and column() simply pull their data from self.rows and self.columns.
Example:
* M = Matrix("1 2 3\n4 5 6\n7 8 9") (-> ["1 2 3", "4 5 6", "7 8 9"] -> [[1, 2, 3], [4, 5, 6], [7, 8, 9]] -> [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
* M.row(2) -> [4, 5, 6]
* M.column(3) -> [3, 6, 9]
"""

class Matrix:

    def __init__(self, matrix_string): # 1 2 3\n4 5 6\n7 8 9
        self.rows = matrix_string.split("\n") #split = ["1 2 3","4 5 6","7 8 9"]
        self.columns = list()
        for r in range(len(self.rows)):
            self.rows[r] = self.rows[r].split(" ")
            for s in range(len(self.rows[r])):
                self.rows[r][s] = int(self.rows[r][s])
        for c in range(len(self.rows[0])):
            self.columns.append([])
        for c in range(len(self.columns)):
            for r in self.rows:
                self.columns[c].append(r[c])

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]