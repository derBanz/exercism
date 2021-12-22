"""
Set task: A kindergarten class has a garden, each student (String) has a square to take care off. When given a student name, return the plants they decided to plant.
Method:
* On initalisation of the garden we create self.students (dict) to store each student's plants.
* Going through a sorted list of the students we assign the first two values per row in the diagram (String) to each student, removing them from the diagram after.
* plants(student) then grabs the student's entry from self.students.
Example:
* G = Garden("CCVG\nRVGG) (-> {"Alice": ["Clover", "Clover", "Radishes", "Violets"], "Bob": ["Violets", "Grass", "Grass", "Grass"]})
* G.plants("Bob") -> ["Violets", "Grass", "Grass", "Grass"]
"""

class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        students=sorted(students)
        self.students=dict()
        plant_names={
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets"
        }
        for s in students:
            self.students[s]=list()
            for p in [diagram[0],diagram[1],diagram[diagram.find("\n")+1],diagram[diagram.find("\n")+2]]:
                self.students[s].append(plant_names[p])
            diagram=diagram[2:diagram.find("\n")+1:]+diagram[diagram.find("\n")+3::]
            if diagram == "\n":
                break

    def plants(self,student):
        return self.students[student]