class Matrix:

    def __init__(self, matrix_string): # 1 2 3\n4 5 6\n7 8 9
        self.split = matrix_string.split("\n") #split = ["1 2 3","4 5 6","7 8 9"]
        for r in range(len(self.split)):
            self.split[r]=self.split[r].split(" ")
        for r in range(len(self.split)):
            for s in range(len(self.split[0])):
                self.split[r][s]=int(self.split[r][s])

    def row(self, index):
        return self.split[index-1]

    def column(self, index):
        result=[]
        for r in range(len(self.split)):
            result.append(self.split[r][index-1])
        return result