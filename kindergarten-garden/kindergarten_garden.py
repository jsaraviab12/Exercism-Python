
class Garden:
    students_source = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", 
                       "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
    plants_type = {"G":"Grass", "C":"Clover", "R":"Radishes", "V":"Violets"}
    def __init__(self, diagram, students = students_source, plants_type = plants_type):
        students.sort()
        self.diagram = diagram.split()
        self.students = students
        self.plants_type = plants_type
        
    def plants(self, name):
        pindex= self.students.index(name)
        return [self.plants_type.get(j) for i in [x[pindex*2] + x[pindex*2+1] 
                for x in self.diagram] for j in i]