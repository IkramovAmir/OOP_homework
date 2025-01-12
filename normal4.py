class Students:
    def __init__(self, name, course, average_mark, grant) -> None:
        self.name = name
        self.course = course
        self.average_mark = average_mark
        self.grant = grant
        
    def printt(self):
        if student.average_mark > 80 and 1000000 < student.grant:
                print(f"{student.name} {student.course}, {student.average_mark}, {student.grant}")
        

student1 = Students("Amir", "Frontend", 84.5, 1200000)
student2 = Students("Zarrux", "backend", 90.0, 1500000)
student3 = Students("Asadbek", "Bootcamp", 79.5, 300000)
student4 = Students("Hamdam", "SMM", 80.0, 450000)
student5 = Students("Hamdam", "SMMPro", 85.0, 1350000)
students = [student1, student2, student3, student4, student5]
    
for student in students:
    student.printt()  # average mark higher than 80 and grant is more than 1000000