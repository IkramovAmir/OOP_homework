class Students:
    def __init__(self, name, age, grades) -> None:
        self.name = name
        self.age = age
        self.grades = grades
        
    def get_average(self):
        total = sum(self.grades) / len(self.grades)
        return total
    
    def is_passing(self):
        return self.get_average() > 60
    

student1 = Students("Amir", 19, [85, 90, 100, 84])
student2 = Students("Zarrux", 27, [50, 35, 75, 69])
student3 = Students("Asadbek", 21, [80, 90, 100, 84])
student4 = Students("Hamdam", 24, [95, 79, 100, 100])
students = [student1, student2, student3, student4]

for student in students:
    print(f"{student.name} {student.get_average()} {student.is_passing()} ")