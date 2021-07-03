class School:
    def __init__(self):
        self.students=[[],[],[],[],[],[],[],[],[]]

    def add_student(self, name, grade):
        self.students[grade-1].append(name)

    def roster(self):
        l=[]
        for i in range(len(self.students)):
            for j in range(len(self.students[i])):
                l.append(sorted(self.students[i])[j])
        return l

    def grade(self, grade_number):
        l=[]
        for i in range(len(self.students[grade_number-1])):
            l.append(sorted(self.students[grade_number-1])[i])
        return l