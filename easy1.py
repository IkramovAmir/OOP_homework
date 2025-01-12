import colorama
class Student:
    
    def __init__(self, full_name, course, mark) -> None:
        self.full_name = full_name
        self.course = course
        self.mark = mark
        
    def full_names(self):
        return self.full_name
    

student1 = Student("Ikramov Amir", "Fullstack", 100)
student2 = Student("Khaydarov Aziz", "Frontend", 105)
student3 = Student("Shomurodov Eldor", "Backend", 90)
student4 = Student("Hikmatov Haydar", "Fullstack", 100)

students = [student1, student2, student3, student4]

for student in students:
    print(colorama.Fore.CYAN  + student.full_names() + colorama.Style.RESET_ALL) #used colorama for printing a bit beautiful