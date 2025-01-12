class School:
    
    def __init__(self, school_name= None, student_name= None) -> None:
        self.school_name = school_name
        self.student_name= student_name
        
    def add_student(self):
        self.student_name = input("Enter new student name: ")
    
    def add_school(self):
        self.school_name = input("Enter new school name: ")
        
    def remove_student(self, student_name):
        for student in students:
            if student.student_name == student_name:
                students.remove(student)  
                print("Student removed successfully!")
                
            else:
                print('Student is not found!!!')
    
    def remove_school(self, school_name):
        for school in schools:
            if school.school_name == school_name:
                schools.remove(school)
                print("School removed successfully!")
            else:
                print("School is not found!!!")
                              
    def show_student(self):
            print(self.school_name)
            for student in students:
                print(student.student_name)


students = []
schools = []
n = int(input("how many schools do u add: "))

for i in range(n):
    school = School()
    school.add_school()
    schools.append(school)
    n2 = int(input("How many students do u add for this school: "))
    for a in range(n2):
        student = School()
        student.add_student()
        students.append(student)

for school in schools:
    school.show_student()
    
n5 = int(input("If you wanna discard student enter 1 or for school enter 2 , to miss just enter random number: "))

count = 0
if n5 == 1:
    st = input("Enter student name to remove: ")
    School().remove_student(st)
elif n5 == 2:
    sch = input("Enter school name to remove: ")
    School().remove_school(sch)

for school in schools:
    school.show_student()