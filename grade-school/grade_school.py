"""
Set task: Model a school with different grades, and monitor which students are in which grade.
Method:
* On initiate, self.students (list) gets created including nine lists.
* add_student adds a student name to the grade's slot in self.students.
* roster returns a list of all students sorted by grade and alphabetically.
* grade returns a list of all students of that grade sorted alphabetically.
Example:
* S = School() (-> [[],[],[],[],[],[],[],[],[]])
* S.add_student("Martin", 2) (-> [[],["Martin"],[],[],[],[],[],[],[]])
* S.add_student("Klaus", 2), S.add_student("Martha",2), S.add_student("Anita", 3), S.add_student("Simon", 1)) (-> [["Simon"], ["Martin", "Klaus", "Martha"], ["Anita"],[],[],[],[],[],[]])
* S.grade(2) -> ["Klaus", "Martha", "Martin"]
* S.roster() -> ["Simon", "Klaus", "Martha", "Martin", "Anita"]
"""

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