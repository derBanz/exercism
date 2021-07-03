class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram=diagram
        self.students=sorted(students)
        self.plant_names={
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets"
        }

    def plants(self,student):
        student_plants=list()
        student_plants.append(self.plant_names[self.diagram[2*self.students.index(student)]])
        student_plants.append(self.plant_names[self.diagram[2*self.students.index(student)+1]])
        student_plants.append(self.plant_names[self.diagram[self.diagram.find("\n")+2*self.students.index(student)+1]])
        student_plants.append(self.plant_names[self.diagram[self.diagram.find("\n")+2*self.students.index(student)+2]])
        return student_plants

G=Garden("CCVC\nGCRV")
print(G.plants("Bob"))